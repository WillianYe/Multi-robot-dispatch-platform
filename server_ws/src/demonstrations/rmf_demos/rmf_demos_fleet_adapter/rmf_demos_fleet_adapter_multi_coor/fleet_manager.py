#!/usr/bin/env python3

# Copyright 2021 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
import math
import yaml
import json
import time
import copy
import argparse
import nudged

import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_system_default

from rclpy.qos import QoSProfile
from rclpy.qos import QoSHistoryPolicy as History
from rclpy.qos import QoSDurabilityPolicy as Durability
from rclpy.qos import QoSReliabilityPolicy as Reliability

from rmf_fleet_msgs.msg import RobotState, Location, PathRequest, \
    DockSummary, RobotMode, FleetState

import rmf_adapter as adpt
import rmf_adapter.vehicletraits as traits
import rmf_adapter.geometry as geometry

import numpy as np
from pyproj import Transformer

import socketio

from fastapi import FastAPI
import uvicorn
from typing import Optional
from pydantic import BaseModel

import threading
app = FastAPI()


class Request(BaseModel):
    map_name: Optional[str] = None
    task: Optional[str] = None
    destination: Optional[dict] = None
    data: Optional[dict] = None
    speed_limit: Optional[float] = None
    toggle: Optional[bool] = None


class Response(BaseModel):
    data: Optional[dict] = None
    success: bool
    msg: str


# ------------------------------------------------------------------------------
# Fleet Manager
# ------------------------------------------------------------------------------
class State:
    def __init__(self, state: RobotState = None, destination: Location = None):
        self.state = state
        self.destination = destination
        self.last_path_request = None
        self.last_completed_request = None
        self.mode_teleop = False
        self.svy_transformer = Transformer.from_crs('EPSG:4326', 'EPSG:3414')
        self.gps_pos = [0, 0]

    def gps_to_xy(self, gps_json: dict):
        svy21_xy = \
            self.svy_transformer.transform(gps_json['lat'], gps_json['lon'])
        self.gps_pos[0] = svy21_xy[1]
        self.gps_pos[1] = svy21_xy[0]

    def is_expected_task_id(self, task_id):
        if self.last_path_request is not None:
            if task_id != self.last_path_request.task_id:
                return False
        return True


class FleetManager(Node):
    def __init__(self, config, nav_path):
        self.debug = False
        self.config = config
        self.fleet_name = self.config["rmf_fleet"]["name"]

        self.gps = False
        self.offset = [0, 0]
        if 'reference_coordinates' in self.config and \
                'offset' in self.config['reference_coordinates']:
            assert len(self.config['reference_coordinates']['offset']) > 1, \
                ('Please ensure that the offset provided is valid.')
            self.gps = True
            self.offset = self.config['reference_coordinates']['offset']

        super().__init__(f'{self.fleet_name}_fleet_manager')

        self.robots = {}  # Map robot name to state
        self.docks = {}  # Map dock name to waypoints
        self.transforms = {}

        for robot_name, robot_config in self.config["robots"].items():
            self.robots[robot_name] = State()
            '''
            if 'reference_coordinates' in robot_config and \
                'rmf' in robot_config['reference_coordinates'] and \
                    'robot' in robot_config['reference_coordinates']:
                rmf_coordinates = robot_config['reference_coordinates']['rmf']
                robot_coordinates = robot_config['reference_coordinates']['robot']
            else:
                rmf_coordinates = [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
                robot_coordinates = [[0.0, 0.0], [
                    1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
            transforms = {
                'rmf_to_robot': nudged.estimate(rmf_coordinates, robot_coordinates),
                'robot_to_rmf': nudged.estimate(robot_coordinates, rmf_coordinates)}
            transforms['orientation_offset'] = \
                transforms['rmf_to_robot'].get_rotation()
            self.get_logger().info("RMF to Robot transform "+str(robot_name)+":")
            self.get_logger().info(
                f"    rotation:{transforms['rmf_to_robot'].get_rotation()}")
            self.get_logger().info(
                f"    scale:{transforms['rmf_to_robot'].get_scale()}")
            self.get_logger().info(
                f"    trans:{transforms['rmf_to_robot'].get_translation()}")
            self.get_logger().info("Robot to RMF transform:")
            self.get_logger().info(
                f"    rotation:{transforms['robot_to_rmf'].get_rotation()}")
            self.get_logger().info(
                f"    scale:{transforms['robot_to_rmf'].get_scale()}")
            self.get_logger().info(
                f"    trans:{transforms['robot_to_rmf'].get_translation()}")
            self.transforms[robot_name]=transforms
            '''
        assert (len(self.robots) > 0)

        profile = traits.Profile(geometry.make_final_convex_circle(
            self.config['rmf_fleet']['profile']['footprint']),
            geometry.make_final_convex_circle(
                self.config['rmf_fleet']['profile']['vicinity']))
        self.vehicle_traits = traits.VehicleTraits(
            linear=traits.Limits(
                *self.config['rmf_fleet']['limits']['linear']),
            angular=traits.Limits(
                *self.config['rmf_fleet']['limits']['angular']),
            profile=profile)
        self.vehicle_traits.differential.reversible =\
            self.config['rmf_fleet']['reversible']


        # Transforms
        if 'reference_coordinates' in self.config and \
            'rmf' in self.config['reference_coordinates'] and \
                'robot' in self.config['reference_coordinates']:
            rmf_coordinates = self.config['reference_coordinates']['rmf']
            robot_coordinates = self.config['reference_coordinates']['robot']
        else:
            rmf_coordinates = [[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
            robot_coordinates = [[0.0, 0.0], [
                1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]
        transforms = {
            'rmf_to_robot': nudged.estimate(rmf_coordinates, robot_coordinates),
            'robot_to_rmf': nudged.estimate(robot_coordinates, rmf_coordinates)}
        transforms['orientation_offset'] = \
            transforms['rmf_to_robot'].get_rotation()
        mse = nudged.estimate_error(transforms['rmf_to_robot'],
                                    rmf_coordinates,
                                    robot_coordinates)
        self.get_logger().info(f"Coordinate transformation error: {mse}")
        self.get_logger().info("RMF to Robot transform:")
        self.get_logger().info(
            f"    rotation:{transforms['rmf_to_robot'].get_rotation()}")
        self.get_logger().info(
            f"    scale:{transforms['rmf_to_robot'].get_scale()}")
        self.get_logger().info(
            f"    trans:{transforms['rmf_to_robot'].get_translation()}")
        self.get_logger().info("Robot to RMF transform:")
        self.get_logger().info(
            f"    rotation:{transforms['robot_to_rmf'].get_rotation()}")
        self.get_logger().info(
            f"    scale:{transforms['robot_to_rmf'].get_scale()}")
        self.get_logger().info(
            f"    trans:{transforms['robot_to_rmf'].get_translation()}")
        self.transforms = transforms

        self.sio = socketio.Client()

        @self.sio.on("/gps")
        def message(data):
            try:
                robot = json.loads(data)
                robot_name = robot['robot_id']
                self.robots[robot_name].gps_to_xy(robot)
            except KeyError as e:
                self.get_logger().info(f"Malformed GPS Message!: {e}")

        if self.gps:
            while True:
                try:
                    self.sio.connect('http://0.0.0.0:8080')
                    break
                except Exception:
                    self.get_logger().info(
                        f"Trying to connect to sio server at"
                        f"http://0.0.0.0:8080..")
                    time.sleep(1)

        self.create_subscription(
            FleetState,
            'turtlebot3_fleet_states',
            self.fleet_state_cb,
            100)

        transient_qos = QoSProfile(
            history=History.KEEP_LAST,
            depth=1,
            reliability=Reliability.RELIABLE,
            durability=Durability.TRANSIENT_LOCAL)

        self.create_subscription(
            DockSummary,
            'dock_summary',
            self.dock_summary_cb,
            qos_profile=transient_qos)

        self.path_pub = self.create_publisher(
            PathRequest,
            'robot_path_requests',
            qos_profile=qos_profile_system_default)

        @app.get('/open-rmf/rmf_demos_fm/status/',
                 response_model=Response)
        async def status(robot_name: Optional[str] = None):
            response = {
                'data': {},
                'success': False,
                'msg': ''
            }
            if robot_name is None:
                self.get_logger().info("robot name is none")   
                response['data']['all_robots'] = []
                for robot_name in self.robots:
                    state = self.robots.get(robot_name)
                    if state is None or state.state is None:
                        return response
                    response['data']['all_robots'].append(
                        self.get_robot_state(state, robot_name))
            else:
                self.get_logger().info("robot name is not none")  
                state = self.robots.get(robot_name)
                if state is None or state.state is None:
                    self.get_logger().info("robot state is none")  
                    return response
                response['data'] = self.get_robot_state(state, robot_name)
            response['success'] = True
            return response

        @app.post('/open-rmf/rmf_demos_fm/navigate/',
                  response_model=Response)
        async def navigate(robot_name: str, cmd_id: int, dest: Request):
            response = {'success': False, 'msg': ''}
            if (robot_name not in self.robots or len(dest.destination) < 1):
                return response

            path_request = PathRequest()
            robot = self.robots[robot_name]
            t=copy.deepcopy(robot.state.location.t)
            cur_loc = copy.deepcopy(robot.state.location)
            [cur_loc.x, cur_loc.y] = self.transforms[robot_name]["rmf_to_robot"].transform(
                [cur_loc.x, cur_loc.y])
            cur_loc.yaw += self.transforms[robot_name]['orientation_offset']
            path_request.path.append(cur_loc)

            [target_x, target_y] =self.transforms[robot_name]["rmf_to_robot"].transform(
                [dest.destination['x'], dest.destination['y']])
            target_yaw = copy.deepcopy(dest.destination['yaw'])
            target_yaw += self.transforms[robot_name]['orientation_offset']
            target_map = dest.map_name
            target_speed_limit = dest.speed_limit

            target_x -= self.offset[0]
            target_y -= self.offset[1]

            disp = self.disp([target_x, target_y], [cur_loc.x, cur_loc.y])
            duration = int(disp/self.vehicle_traits.linear.nominal_velocity) +\
                int(abs(abs(cur_loc.yaw) - abs(target_yaw)) /
                    self.vehicle_traits.rotational.nominal_velocity)
            self.get_logger().info("current time sec when sending navigate request:"+str(t.sec))
            self.get_logger().info("navigate request duration:"+str(duration))            
            t.sec = t.sec + duration
            target_loc = Location()
            target_loc.t = t
            target_loc.x = target_x
            target_loc.y = target_y
            target_loc.yaw = target_yaw
            target_loc.level_name = target_map
            if target_speed_limit > 0:
                target_loc.obey_approach_speed_limit = True
                target_loc.approach_speed_limit = target_speed_limit

            path_request.fleet_name = self.fleet_name
            path_request.robot_name = robot_name
            path_request.path.append(target_loc)
            path_request.task_id = str(cmd_id)
            self.path_pub.publish(path_request)
            self.get_logger().info(
                f'Sending navigate request for {robot_name}: {cmd_id} to {target_x},{target_y},{target_yaw}')

            robot.last_path_request = path_request

            robot.destination = copy.deepcopy(target_loc)
            [robot.destination.x, robot.destination.y] = self.transforms[robot_name]['robot_to_rmf'].transform(
                [robot.destination.x, robot.destination.y])
            robot.destination.yaw -= self.transforms[robot_name]['orientation_offset']
            response['success'] = True
            return response

        @app.get('/open-rmf/rmf_demos_fm/stop_robot/',
                 response_model=Response)
        async def stop(robot_name: str, cmd_id: int):
            response = {'success': False, 'msg': ''}
            if robot_name not in self.robots:
                return response

            robot = self.robots[robot_name]
            path_request = PathRequest()
            path_request.fleet_name = self.fleet_name
            path_request.robot_name = robot_name
            path_request.path = []
            # Appending the current location twice will effectively tell the
            # robot to stop
            cur_loc = copy.deepcopy(robot.state.location)
            [cur_loc.x, cur_loc.y] = self.transforms[robot_name]["rmf_to_robot"].transform(
                [cur_loc.x, cur_loc.y])
            cur_loc.yaw +=self.transforms[robot_name]['orientation_offset']

            path_request.path.append(cur_loc)
            path_request.path.append(cur_loc)

            path_request.task_id = str(cmd_id)
            self.path_pub.publish(path_request)

            self.path_pub.publish(path_request)
            self.get_logger().info(
                f'Sending stop request for {robot_name}: {cmd_id} to {cur_loc.x},{cur_loc.y},{cur_loc.yaw}')
            robot.last_path_request = path_request
            robot.destination = None

            response['success'] = True
            return response

        @app.post('/open-rmf/rmf_demos_fm/start_task/',
                  response_model=Response)
        async def start_process(robot_name: str, cmd_id: int, task: Request):
            response = {'success': False, 'msg': ''}
            if (robot_name not in self.robots or
                    len(task.task) < 1 or
                    task.task not in self.docks):
                return response

            robot = self.robots[robot_name]

            path_request = PathRequest()
            cur_loc = copy.deepcopy(robot.state.location)
            [cur_loc.x, cur_loc.y] =self.transforms[robot_name]["rmf_to_robot"].transform(
                [cur_loc.x, cur_loc.y])
            cur_loc.yaw +=self.transforms[robot_name]['orientation_offset']
            path_request.path.append(cur_loc)

            target_loc = Location()
            for wp in self.docks[task.task]:
                target_loc = copy.deepcopy(wp)
                [target_loc.x, target_loc.y] =self.transforms[robot_name]["rmf_to_robot"].transform([
                                                                                    target_loc.x, target_loc.y])
                target_loc.yaw +=self.transforms[robot_name]['orientation_offset']
                path_request.path.append(target_loc)

            path_request.fleet_name = self.fleet_name
            path_request.robot_name = robot_name
            path_request.task_id = str(cmd_id)
            self.path_pub.publish(path_request)

            self.get_logger().info(
                f'Sending process request for {robot_name}: {cmd_id}')
            robot.last_path_request = path_request

            robot.destination = copy.deepcopy(target_loc)
            [robot.destination.x, robot.destination.y] = self.transforms[robot_name]['robot_to_rmf'].transform(
                [robot.destination.x, robot.destination.y])
            robot.destination.yaw -=self.transforms[robot_name]['orientation_offset']

            response['success'] = True
            return response

        @app.post('/open-rmf/rmf_demos_fm/toggle_action/',
                  response_model=Response)
        async def toggle_teleop(robot_name: str, mode: Request):
            response = {'success': False, 'msg': ''}
            if (robot_name not in self.robots):
                return response
            # Toggle action mode
            self.robots[robot_name].mode_teleop = mode.toggle
            response['success'] = True
            return response

    def fleet_state_cb(self, msg):
        if (msg.name == self.fleet_name):
            for robot_state in msg.robots:
                if (robot_state.name in self.robots):
                    robot = self.robots[robot_state.name]
                    if not robot.is_expected_task_id(robot_state.task_id) and \
                            not robot.mode_teleop:
                        # This message is out of date, so disregard it.
                        if robot.last_path_request is not None:
                            # Resend the latest task request for this robot, in case
                            # the message was dropped.
                            '''
                            self.get_logger().info(
                                f'Republishing task request for {robot_state.name}: '
                                f'{robot.last_path_request.task_id}, '
                                f'because it is currently following {robot_state.task_id}'
                            )
                            '''
                            self.path_pub.publish(robot.last_path_request)
                        return

                    robot.state = robot_state
                    [robot.state.location.x, robot.state.location.y] = self.transforms[robot_state.name]['robot_to_rmf'].transform(
                        [robot_state.location.x, robot_state.location.y])
                    robot.state.location.yaw -=self.transforms[robot_state.name]['orientation_offset']

                    # Check if robot has reached destination
                    if robot.destination is None:
                        return

                    if (
                        (
                            robot_state.mode.mode == RobotMode.MODE_IDLE
                            or robot_state.mode.mode == RobotMode.MODE_CHARGING
                        )
                        and len(robot_state.path) == 0
                    ):
                        robot.destination = None
                        completed_request = int(robot_state.task_id)
                        if robot.last_completed_request != completed_request:
                            self.get_logger().info(
                                f'Detecting completed request for {robot_state.name}: '
                                f'{completed_request}'
                            )
                        robot.last_completed_request = completed_request

    def dock_summary_cb(self, msg):
        for fleet in msg.docks:
            if (fleet.fleet_name == self.fleet_name):
                for dock in fleet.params:
                    self.docks[dock.start] = dock.path

    def get_robot_state(self, robot: State, robot_name):
        data = {}
        if self.gps:
            position = copy.deepcopy(robot.gps_pos)
        else:
            position = [robot.state.location.x, robot.state.location.y]
        data['robot_name'] = robot_name
        data['map_name'] = robot.state.location.level_name
        yaw = robot.state.location.yaw
        data['position'] =\
            {'x': position[0], 'y': position[1], 'yaw': yaw}
        # data['battery'] = robot.state.battery_percent
        data['battery'] = 100.0
        if (robot.destination is not None
                and robot.last_path_request is not None):
            destination = robot.destination
            # remove offset for calculation if using gps coords
            if self.gps:
                position[0] -= self.offset[0]
                position[1] -= self.offset[1]
            # calculate arrival estimate
            dist_to_target =\
                self.disp(position, [destination.x, destination.y])
            ori_delta = abs(abs(yaw) - abs(destination.yaw))
            if ori_delta > np.pi:
                ori_delta = ori_delta - (2 * np.pi)
            if ori_delta < -np.pi:
                ori_delta = (2 * np.pi) + ori_delta
            duration = (dist_to_target /
                        self.vehicle_traits.linear.nominal_velocity +
                        ori_delta /
                        self.vehicle_traits.rotational.nominal_velocity)
            cmd_id = int(robot.last_path_request.task_id)
            data['destination_arrival'] = {
                'cmd_id': cmd_id,
                'duration': duration
            }
        else:
            data['destination_arrival'] = None

        data['last_completed_request'] = robot.last_completed_request
        if (
            robot.state.mode.mode == RobotMode.MODE_WAITING
            or robot.state.mode.mode == RobotMode.MODE_ADAPTER_ERROR
        ):
            # The name of MODE_WAITING is not very intuitive, but the slotcar
            # plugin uses it to indicate when another robot is blocking its
            # path.
            #
            # MODE_ADAPTER_ERROR means the robot received a plan that
            # didn't make sense, i.e. the plan expected the robot was starting
            # very far from its real present location. When that happens we
            # should replan, so we'll set replan to true in that case as well.
            data['replan'] = True
        else:
            data['replan'] = False

        return data

    def disp(self, A, B):
        return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------
def main(argv=sys.argv):
    # Init rclpy and adapter
    rclpy.init(args=argv)
    adpt.init_rclcpp()
    args_without_ros = rclpy.utilities.remove_ros_args(argv)

    parser = argparse.ArgumentParser(
        prog="fleet_adapter",
        description="Configure and spin up the fleet adapter")
    parser.add_argument("-c", "--config_file", type=str, required=True,
                        help="Path to the config.yaml file")
    parser.add_argument("-n", "--nav_graph", type=str, required=True,
                        help="Path to the nav_graph for this fleet adapter")
    args = parser.parse_args(args_without_ros[1:])
    print(f"Starting fleet manager...")

    with open(args.config_file, "r") as f:
        config = yaml.safe_load(f)

    fleet_manager = FleetManager(config, args.nav_graph)

    spin_thread = threading.Thread(target=rclpy.spin, args=(fleet_manager,))
    spin_thread.start()

    uvicorn.run(app,
                host=config['rmf_fleet']['fleet_manager']['ip'],
                port=config['rmf_fleet']['fleet_manager']['port'],
                log_level='warning')


if __name__ == '__main__':
    main(sys.argv)