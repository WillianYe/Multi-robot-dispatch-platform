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

"""
This simple schema validation script shows a simple example of validating
json input with the existing "task_state" and "task_logs" schemas, 
defined in rmf_api_msgs.
"""

import json
import sys
import argparse

from jsonschema import validate
from rmf_api_msgs import schemas


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--task_log", action="store_true",
                        help='validate task log')
    parser.add_argument("--task_state", action="store_true",
                        help='validate task state')
    parser.add_argument('-i', '--input', required=True,
                        type=str, help='json file input path')
    args = parser.parse_args(argv[1:])

    if args.task_state:
        print("checking input json with [task_state] schema")
        schema = schemas.task_state()
    elif args.task_log:
        print("checking input json with [task_log] schema")
        schema = schemas.task_log()
    else:
        print("Error, No schema selection is chosen, exit")
        parser.print_help()
        exit(0)

    schema = json.loads(schema)

    # load input file
    file = open(args.input)
    data = json.load(file)
    file.close()

    error = validate(instance=data, schema=schema)
    if not error:
        print(f"Validated [{args.input}]. It's Good!")

###############################################################################


if __name__ == "__main__":
    main(sys.argv)
