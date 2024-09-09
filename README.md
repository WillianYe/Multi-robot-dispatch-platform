# 多智能轮椅调度云平台
该项目可作为基于ros1的多移动机器人调度云平台的范例。

以上海交通大学自主机器人实验室的智能轮椅为对象，基于[n2n](https://github.com/ntop/n2n)虚拟局域网和ros2的[open-rmf](https://github.com/open-rmf/rmf_demos)框架开发智能轮椅调度的云平台，实现轮椅的状态监控，数台轮椅之间的任务分配和路径规划。

<img width="300" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/img1.png"/></div>

1.任务分配：用户在云平台提供的GUI上发布移动任务，云平台将任务分配给各个轮椅。

2.路径规划：根据建筑设计图或SLAM建图，画出路线图，云平台在路线图上规划路径，目的是防止轮椅死锁与碰撞。

3.状态监控：在GUI和路线图上实时显示轮椅位置、电量、任务完成程度等信息。

## 运行效果
### GUI和路线图
<img width="700" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/img4.png" alt="GUI"/></div>
<img width="700" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/img5.png" alt="路线图示例，可基于SLAM或设计图"/></div>

以下gif加载可能需要一定时间。

### gazebo仿真
<img width="700" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/img6.png"/></div>
<img width="700" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/gif1.gif"/></div>
### 实物仿真
<img width="700" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/gif2.gif"/></div>

## 云平台架构
<img width="700" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/img2.png"/></div>
<img width="700" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/img3.png"/></div>

## 安装
示例配置为：
+ 轮椅系统:ubuntu 18.04+ros1 melodic，使用[move_base](https://wiki.ros.org/move_base)进行单机器人导航
+ 云平台系统:ubuntu 20.04+ros2 foxy
+ 云服务器（带有公网ip）

### 云平台和轮椅的通讯
考虑到智能轮椅在医院部署时的网络通讯问题（电梯等），采用虚拟局域网。

云服务器+轮椅+云平台的部署：
```sh
mkdir ~/tools
cd ~/tools/
git clone -b 3.0-stable https://ghproxy.com/https://github.com/ntop/n2n n2n-3.0
cd n2n-3.0
./autogen.sh
./configure
make
```
部署后进行连接，云服务器端（其中5000是端口号，需替换）：
```sh
cd ~/tools/n2n-3.0
sudo ./supernode -p 5000 -f -vvv
```
云平台端（其中124.222.129.117是公网ip，需替换）：
```sh
cd ~/tools/n2n-3.0
sudo ./edge -a 10.0.0.3 -c g1 -k test -l 124.222.129.117:5000 -f -vvv
```
轮椅端：
```sh
cd ~/tools/n2n-3.0
sudo ./edge -a 10.0.0.4 -c g1 -k test -l 124.222.129.117:5000 -f -vvv
```
检测是否连接：
```sh
ping 10.0.0.4
ping 10.0.0.3
```

### 云平台和轮椅ros消息通讯
该模块用于解决云平台和轮椅ros版本不一致导致的消息通讯问题。

首先，轮椅端需要安装ros2系统，推荐用[鱼香ros](https://fishros.com/)安装ros2 eloquent版本：
```sh
wget http://fishros.com/install -O fishros && . fishros
```

ros1和ros2的消息通讯基于[cyclonedds](https://github.com/eclipse-cyclonedds/cyclonedds)机制。
轮椅安装cyclonedds：
```sh
sudo apt-get install ros-eloquent-rmw-cyclonedds-cpp
```

云平台安装cyclonedds：
```sh
sudo apt-get install ros-foxy-rmw-cyclonedds-cpp
```

cyclonedds参数配置，其中cyclonedds.xml已在本项目文件中给出范例，增加机器人个数时均需修改cyclonedds.xml：
```sh
echo "export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp " >> ~/.bashrc
echo "export CYCLONEDDS_URI=file:///home/***/cyclonedds.xml " >> ~/.bashrc
```

部署完成后测试通讯：
```sh
ros2 run demo_nodes_cpp talker
ros2 run demo_nodes_cpp listener
```

轮椅内部的ros1系统和ros2系统基于[ros1_bridge](https://github.com/ros2/ros1_bridge)。
轮椅端安装 ros1_bridge：
```sh
source /opt/ros/eloquent/setup.bash
sudo apt-get install ros-eloquent-ros1-bridge
```

安装后测试，轮椅端：
终端 1：
```sh
source /opt/ros/melodic/setup.bash
roscore
```
终端 2（其中11311要根据roscore信息修改）：
```sh
source /opt/ros/melodic/setup.bash
source /opt/ros/eloquent/setup.bash
export ROS_MASTER_URI=http://localhost:11311
ros2 run ros1_bridge dynamic_bridge
```

测试ROS 1 talker and ROS 2 listener，
终端 3：
```sh
source /opt/ros/melodic/setup.bash
rosrun rospy_tutorials talker
```
终端 4：
```sh
source /opt/ros/eloquent/setup.bash
ros2 run demo_nodes_cpp listener
```

测试ROS 2 talker and ROS 1 listener，
终端 3：
```sh
source /opt/ros/eloquent/setup.bash
ros2 run demo_nodes_py talker
```
终端 4：
```sh
source /opt/ros/melodic/setup.bash
rosrun roscpp_tutorials listener
```
### 仿真实验
将本项目中的"client_ws"文件夹放入ros1（移动机器人）的工作空间，"server_ws"文件夹放入ros2（调度平台）的工作空间，并分别采用catkin_make和colcon build编译。

在ros1端：
```sh
cd ~/client_ws
source install/setup.bash
export TURTLEBOT3_MODEL=burger; roslaunch ff_examples_ros1 multi_turtlebot3_ff.launch
```
在ros2端，终端1：
```sh
cd ~/server_ws
source install/setup.bash
ros2 launch ff_examples_ros2 turtlebot3_world_ff_server.launch.xml
```

ros2端，终端2：
```sh
cd ~/server_ws
source install/setup.bash
ros2 launch rmf_demos world.launch.xml
```

ros2端开启GUI：
```sh
cd ~/server_ws/rmf-panel-js/rmf_panel
python3 -m http.server 3000
```

在[网页端](http://localhost:3000/)中可查看GUI。
效果如下：

<img width="700" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/gif3.gif"/></div>
### 自定义路线图

可采用[traffic_editor](https://github.com/open-rmf/rmf_traffic_editor)定义自己的路线图。本项目以自定义的house地图为例。 

建立好的路线图存放在server_ws/src/demonstrations/rmf_demos/rmf_demos_maps/maps/，然后建立nav graph：
```sh
ros2 run rmf_building_map_tools building_map_generator nav ~/server_ws/src/demonstrations/rmf_demos/rmf_demos_maps/maps/house/house.building.yaml ~/server_ws/install/rmf_demos_maps/share/rmf_demos_maps/maps/house/nav_graph
```
在server_ws/src/demonstrations/rmf_demos/rmf_demos/launch文件夹中新增对应地图的launch文件。根据launch文件内容修改相应文件并重新编译：
```sh
colcon build --packages-select rmf_demos rmf_demos_maps rmf_demos_dashboard_resources rmf_demos_panel
```
运行指令参照“仿真实验”部分，更换launch文件：
```sh
ros2 launch rmf_demos house.launch.xml
```
效果如下：

<img width="700" src="https://github.com/WillianYe/Multi-intelligent-wheelchair/blob/main/img/gif4.gif"/></div>
### 实地实验
以2台轮椅为例，先让每台轮椅启动导航模块。

云平台：
```sh
cd ~/tools/n2n-3.0
sudo ./edge -a 10.0.0.3 -c g1 -k test -l 106.15.50.124:5000 -f
```
轮椅1：
```sh
cd ~/tools/n2n-3.0
sudo ./edge -a 10.0.0.4 -c g1 -k test -l 106.15.50.124:5000 -f
```
轮椅2：
```sh
cd ~/tools/n2n-3.0
sudo ./edge -a 10.0.0.5 -c g1 -k test -l 106.15.50.124:5000 -f
```
每台轮椅：
```sh
cd ~/client_ws
source install/setup.bash
roslaunch ff_examples_ros1 lunyi.launch
```
云平台：
```sh
ros2 launch ff_examples_ros2 turtlebot3_world_ff_server.launch.xml
ros2 launch rmf_demos imr.launch.xml
cd rmf-panel-js/rmf_panel/
python3 -m http.server 3000
```

