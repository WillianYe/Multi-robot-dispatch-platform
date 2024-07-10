#!/usr/bin/env python3
###############################################################################
# This python module is a self generated script from 
# rmf_api_msgs/scripts/schemas_template.jinja2

import os

###############################################################################
# @Brief: Function to get cancel_task_response json schema
# @return: json schema, in raw string
def cancel_task_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/cancel_task_response.json",
  "title": "Task Cancel Response",
  "description": "Response to a request to cancel a task",
  "$ref": "simple_response.json"
}
"""

###############################################################################
# @Brief: Function to get undo_skip_phase_response json schema
# @return: json schema, in raw string
def undo_skip_phase_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/undo_phase_skip_response.json",
  "title": "Undo Phase Skip Response",
  "description": "Response to an undo phase skip request",
  "$ref": "simple_response.json"
}
"""

###############################################################################
# @Brief: Function to get log_entry json schema
# @return: json schema, in raw string
def log_entry():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/log_entry.json",
  "title": "Log Entry",
  "description": "An entry in the log of an event",
  "type": "object",
  "properties": {
    "seq": {
      "description": "Sequence number for this entry. Each entry has a unique sequence number which monotonically increase, until integer overflow causes a wrap around.",
      "type": "integer",
      "minimum": 0,
      "exclusiveMaximum": 4294967296
    },
    "tier": {
      "description": "The importance level of the log entry",
      "type": "string",
      "enum": ["uninitialized", "info", "warning", "error"]
    },
    "unix_millis_time": { "type": "integer" },
    "text": {
      "description": "The text of the log entry",
      "type": "string"
    }
  },
  "required": ["seq", "tier", "unix_millis_time", "text"]
}
"""

###############################################################################
# @Brief: Function to get robot_task_response json schema
# @return: json schema, in raw string
def robot_task_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/robot_task_response.json",
  "title": "Robot Task Response",
  "description": "Response to a robot task request",
  "$ref": "dispatch_task_response.json"
}
"""

###############################################################################
# @Brief: Function to get fleet_state json schema
# @return: json schema, in raw string
def fleet_state():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/fleet_state.json",
  "title": "Fleet State",
  "description": "The state of a fleet",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "robots": {
      "description": "A dictionary of the states of the robots that belong to this fleet",
      "type": "object",
      "additionalProperties": { "$ref": "robot_state.json" }
    }
  }
}
"""

###############################################################################
# @Brief: Function to get interrupt_task_response json schema
# @return: json schema, in raw string
def interrupt_task_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/interrupt_task_response.json",
  "title": "Task Interruption Response",
  "description": "Response to a request for a task to be interrupted",
  "$ref": "token_response.json"
}
"""

###############################################################################
# @Brief: Function to get robot_task_request json schema
# @return: json schema, in raw string
def robot_task_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/robot_task_request.json",
  "title": "Robot Task Request",
  "description": "Request to be directly assigned to a specific robot",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task dispatch request",
      "type": "string",
      "constant": "robot_task_request"
    },
    "robot": {
      "description": "The name of the robot",
      "type": "string"
    },
    "fleet": {
      "description": "The fleet the robot belongs to",
      "type": "string"
    },
    "request": { "$ref": "task_request.json" }
  },
  "required": ["type", "robot", "fleet", "request"]
}
"""

###############################################################################
# @Brief: Function to get task_discovery_response json schema
# @return: json schema, in raw string
def task_discovery_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_discovery_update.json",
  "title": "Task Discovery",
  "description": "Discovered information about what kinds of tasks a fleet supports",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is an task discovery update",
      "type": "string",
      "enum": ["task_discovery_update"]
    },
    "data": {
      "type": "object",
      "properties": {
        "fleet_name": {
          "description": "Name of the fleet that supports these tasks",
          "type": "string"
        },
        "tasks": {
          "description": "(list:replace) List of tasks that the fleet supports",
          "type": "array",
          "items": { "$ref": "#/$defs/task" }
        }
      }
    }
  },
  "required": ["type", "data"],
  "$defs": {
    "task": {
      "description": "Information about a task",
      "type": "object",
      "properties": {
        "category": {
          "description": "The category of this task. There must not be any duplicate task categories per fleet.",
          "type": "string"
        },
        "detail": {
          "description": "Details about the behavior of the task.",
          "type": "string"
        },
        "description_schema": {
          "description": "The schema for this task description",
          "type": "object"
        }
      },
      "required": ["category", "detail", "schema"]
    }
  }
}
"""

###############################################################################
# @Brief: Function to get token_response json schema
# @return: json schema, in raw string
def token_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/token_response.json",
  "title": "Token Response",
  "description": "Template for defining a response message that provides a token upon success or errors upon failure",
  "type": "object",
  "oneOf": [
    {
      "properties": {
        "success": { "$ref": "#/$defs/success" },
        "token": {
          "description": "A token for the request. The value of this token is unique within the scope of this request and can be used by other requests to reference this request.",
          "type": "string"
        }
      },
      "required": ["success", "token"]
    },
    {
      "properties": {
        "success": { "$ref": "#/$defs/failure" },
        "errors": {
          "description": "Any error messages explaining why the request failed.",
          "type": "array",
          "items": { "$ref": "error.json" }
        }
      },
      "required": ["success", "errors"]
    }
  ],
  "$defs": {
    "success": {
      "description": "The request was successful",
      "type": "boolean",
      "enum": [true]
    },
    "failure": {
      "description": "The request failed",
      "type": "boolean",
      "enum": [false]
    }
  }
}
"""

###############################################################################
# @Brief: Function to get cancel_task_request json schema
# @return: json schema, in raw string
def cancel_task_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/cancel_task_request.json",
  "title": "Cancel Task Request",
  "description": "Ask for a task to be canceled.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task cancellation request",
      "type": "string",
      "enum": ["cancel_task_request"]
    },
    "task_id": {
      "description": "Specify the task ID to cancel",
      "type": "string"
    },
    "labels": {
      "description": "Labels to describe the purpose of the cancellation",
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["type", "task_id"]
}
"""

###############################################################################
# @Brief: Function to get rewind_task_response json schema
# @return: json schema, in raw string
def rewind_task_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/rewind_task_response.json",
  "title": "Task Rewind Response",
  "description": "Response to a request to rewind a task",
  "$ref": "simple_response.json"
}
"""

###############################################################################
# @Brief: Function to get error json schema
# @return: json schema, in raw string
def error():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/error.json",
  "title": "Error",
  "description": "Description of an error that has occurred while handling a request",
  "type": "object",
  "properties": {
    "code": {
      "description": "A standard code for the kind of error that has occurred",
      "type": "integer",
      "minimum": 0
    },
    "category": {
      "description": "The category of the error",
      "type": "string"
    },
    "detail": {
      "description": "Details about the error",
      "type": "string"
    }
  }
}
"""

###############################################################################
# @Brief: Function to get task_request json schema
# @return: json schema, in raw string
def task_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_request.json",
  "title": "Task Request",
  "description": "Describe a task request",
  "type": "object",
  "properties": {
    "unix_millis_earliest_start_time": {
      "description": "(Optional) The earliest time that this task may start",
      "type": "integer"
    },
    "priority": {
      "description": "(Optional) The priority of this task. This must match a priority schema supported by a fleet.",
      "type": "object"
    },
    "category": { "type": "string" },
    "description": {
      "description": "A description of the task. This must match a schema supported by a fleet for the category of this task request."
    },
    "labels": {
      "description": "Labels to describe the purpose of the task dispatch request",
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["category", "description"]
}
"""

###############################################################################
# @Brief: Function to get interrupt_task_request json schema
# @return: json schema, in raw string
def interrupt_task_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/interrupt_task_request.json",
  "title": "Task Interruption Request",
  "description": "Ask for a task to be interrupted. An interrupted task will resume its task later when a resume_task_requested is sent.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task interruption request",
      "type": "string",
      "enum": ["interrupt_task_request"]
    },
    "task_id": {
      "description": "Specify the task ID to interrupt",
      "type": "string"
    },
    "labels": {
      "description": "Labels to describe the purpose of the interruption",
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["type", "task_id"]
}
"""

###############################################################################
# @Brief: Function to get rewind_task_request json schema
# @return: json schema, in raw string
def rewind_task_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/rewind_task_request.json",
  "title": "Task Rewind Request",
  "description": "Ask for a task to rewind itself to an earlier phase.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task rewind request",
      "type": "string",
      "enum": ["rewind_task_request"]
    },
    "task_id": {
      "description": "Specify the ID of the task that should rewind",
      "type": "string"
    },
    "phase_id": {
      "description": "Specify the phase that should be rewound to. The task will restart at the beginning of this phase.",
      "type": "integer",
      "minimum": 0
    }
  },
  "required": ["type", "task_id", "phase_id"]
}
"""

###############################################################################
# @Brief: Function to get rtls_tag_state json schema
# @return: json schema, in raw string
def rtls_tag_state():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/rtls_tag_state.json",
  "title": "Rtls Tag State",
  "description": "The state of a realtime location system tag",
  "type": "object",
  "properties": {
    "tag_id": {
      "description": "The ID of the rtls tag.",
      "type": "string"
    },
    "status": {
      "description": "A simple token representing the status of the tag",
      "type": "string",
      "enum": ["uninitialized", "offline", "shutdown", "idle", "charging", "working", "error"]
    },
    "location_type": {
      "description": "The type location information provided by the tag.",
      "type": "string",
      "enum": ["zone", "coord"]
    },
    "asset_type": {
      "description": "The type of the tagged asset.",
      "type": "object",
      "properties": {
        "asset_type": {
          "description": "type of the asset",
          "type": "string"
        },
        "asset_subtype": {
          "description": "subtype of the asset",
          "type": "string"
        }
      },
      "required": ["type", "subtype"]
    },
    "unix_millis_time": { "type": "integer" },
    "location": { "$ref": "location_2D.json" },
    "battery": {
      "description": "State of charge of the battery. Values range from 0.0 (depleted) to 1.0 (fully charged)",
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "issues": {
      "description": "A list of issues with the tag that operators need to address",
      "type": "array",
      "items": { "$ref": "#/$defs/issue" }
    }
  },
  "required": ["tag_id"],
  "$defs": {
    "issue": {
      "description": "An issue that an operator needs to respond to (e.g. disconnection, lost)",
      "type": "object",
      "properties": {
        "category": {
          "description": "Category of the tag's issue",
          "type": "string"
        },
        "detail": {
          "description": "Detailed information about the issue",
          "anyOf": [
            { "type": "object" },
            { "type": "array" },
            { "type": "string" }
          ]
        }
      }
    }
  }
}
"""

###############################################################################
# @Brief: Function to get skip_phase_response json schema
# @return: json schema, in raw string
def skip_phase_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/skip_phase_response.json",
  "title": "Skip Phase Response",
  "description": "Response to a request for a phase to be skipped",
  "$ref": "token_response.json"
}
"""

###############################################################################
# @Brief: Function to get dispatch_task_request json schema
# @return: json schema, in raw string
def dispatch_task_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/dispatch_task_request.json",
  "title": "Dispatch Task Request",
  "description": "Request that a task be dispatched to the best available fleet",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task dispatch request",
      "type": "string",
      "enum": ["dispatch_task_request"]
    },
    "request": { "$ref": "task_request.json" }
  },
  "required": ["type", "request"]
}
"""

###############################################################################
# @Brief: Function to get dispatch_task_response json schema
# @return: json schema, in raw string
def dispatch_task_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/dispatch_task_response.json",
  "title": "Task Dispatch Response",
  "description": "Response to a task dispatch request",
  "type": "object",
  "oneOf": [
    {
      "properties": {
        "success": { "type": "boolean", "enum": [true] },
        "state": { "$ref": "task_state.json" }
      },
      "required": ["success", "state"]
    },
    {
      "properties": {
        "success": { "type": "boolean", "enum": [false] },
        "errors": {
          "description": "Any error messages explaining why the request failed",
          "type": "array",
          "items": { "$ref": "error.json" }
        }
      }
    }
  ]
}
"""

###############################################################################
# @Brief: Function to get fleet_state_update json schema
# @return: json schema, in raw string
def fleet_state_update():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/fleet_state_update.json",
  "title": "Fleet State Update",
  "description": "Update for the state of a fleet",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a fleet state update",
      "type": "string",
      "enum": ["fleet_state_update"]
    },
    "data": {
      "$ref": "fleet_state.json"
    }
  },
  "required": ["type", "data"]
}
"""

###############################################################################
# @Brief: Function to get fleet_log_request json schema
# @return: json schema, in raw string
def fleet_log_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/fleet_log_request.json",
  "title": "Fleet Log Request",
  "description": "Request the event log for a fleet",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a fleet log request",
      "type": "string",
      "enum": ["fleet_log_request"]
    },
    "fleet": {
      "description": "Specify the name of the fleet whose log should be fetched",
      "type": "string"
    }
  },
  "required": ["type", "fleet"]
}
"""

###############################################################################
# @Brief: Function to get task_log_request json schema
# @return: json schema, in raw string
def task_log_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_log_request.json",
  "title": "Task Log Request",
  "description": "Request the event log for a task",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task log request",
      "type": "string",
      "enum": ["task_log_request"]
    },
    "task_id": {
      "description": "Specify the ID of the task whose log should be fetched",
      "type": "string"
    }
  },
  "required": ["type", "task_id"]
}
"""

###############################################################################
# @Brief: Function to get activity_discovery_request json schema
# @return: json schema, in raw string
def activity_discovery_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/activity_discovery_request.json",
  "title": "Activity Discovery Request",
  "description": "Ask for activities that can be performed by the fleets",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is an activity discovery request",
      "type": "string",
      "enum": ["activitiy_discovery_request"]
    }
  },
  "required": ["type"]
}
"""

###############################################################################
# @Brief: Function to get kill_task_response json schema
# @return: json schema, in raw string
def kill_task_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/kill_task_response.json",
  "title": "Task Kill Response",
  "description": "Response to a request to kill a task",
  "$ref": "simple_response.json"
}
"""

###############################################################################
# @Brief: Function to get task_log_update json schema
# @return: json schema, in raw string
def task_log_update():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_log_update.json",
  "title": "Task Event Log Update",
  "description": "Update for the log of a task. These new entries should be added to any log entries that already existed for each event, ignoring any with a duplicate `seq` value.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is an event log update",
      "type": "string",
      "enum": ["task_log_update"]
    },
    "data": { "$ref": "task_log.json" }
  },
  "required": ["type", "data"]
}
"""

###############################################################################
# @Brief: Function to get fleet_log json schema
# @return: json schema, in raw string
def fleet_log():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/fleet_log.json",
  "title": "Fleet Log",
  "description": "The log of a fleet",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "log": {
      "description": "Log for the overall fleet",
      "type": "array",
      "items": { "$ref": "log_entry.json" }
    },
    "robots": {
      "description": "Dictionary of logs for the individual robots. The keys (property names) are the robot names.",
      "type": "object",
      "additionalProperties": {
        "type": "array",
        "items": { "$ref": "log_entry.json" }
      }
    }
  }
}
"""

###############################################################################
# @Brief: Function to get robot_state json schema
# @return: json schema, in raw string
def robot_state():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/robot_state.json",
  "title": "Robot State",
  "description": "The state of a robot",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "status": {
      "description": "A simple token representing the status of the robot",
      "type": "string",
      "enum": ["uninitialized", "offline", "shutdown", "idle", "charging", "working", "error"]
    },
    "task_id": {
      "description": "The ID of the task this robot is currently working on. Empty string if the robot is not working on a task.",
      "type": "string"
    },
    "unix_millis_time": { "type": "integer" },
    "location": { "$ref": "location_2D.json" },
    "battery": {
      "description": "State of charge of the battery. Values range from 0.0 (depleted) to 1.0 (fully charged)",
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "issues": {
      "description": "A list of issues with the robot that operators need to address",
      "type": "array",
      "items": { "$ref": "#/$defs/issue" }
    }
  },
  "$defs": {
    "issue": {
      "description": "An issue that an operator needs to respond to (e.g. stuck, lost)",
      "type": "object",
      "properties": {
        "category": {
          "description": "Category of the robot's issue",
          "type": "string"
        },
        "detail": {
          "description": "Detailed information about the issue",
          "anyOf": [
            { "type": "object" },
            { "type": "array" },
            { "type": "string" }
          ]
        }
      }
    }
  }
}
"""

###############################################################################
# @Brief: Function to get transformation_2D json schema
# @return: json schema, in raw string
def transformation_2D():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/transformation_2D.json",
  "title": "Transformation 2D",
  "description": "Transformation between 2 maps",
  "type": "object",
  "properties": {
    "target_map": { "type": "string" },
    "ref_map": { "type": "string" },
    "x": { "type": "number" },
    "y": { "type": "number" },
    "yaw": { "type": "number" },
    "scale": { "type": "number" }
  },
  "required": ["target_map", "ref_map", "x", "y", "yaw", "scale"]
}
"""

###############################################################################
# @Brief: Function to get task_log json schema
# @return: json schema, in raw string
def task_log():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_log.json",
  "title": "Task Event Log",
  "description": "Log information for a task",
  "type": "object",
  "properties": {
    "task_id": { "type": "string" },
    "log": {
      "description": "Log entries related to the overall task",
      "type": "array",
      "items": { "$ref": "log_entry.json" }
    },
    "phases": {
      "description": "A dictionary whose keys (property names) are the indices of a phase",
      "type": "object",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "log": {
            "description": "Log entries related to the overall phase",
            "type": "array",
            "items": { "$ref": "log_entry.json" }
          },
          "events": {
            "description": "A dictionary whose keys (property names) are the indices of an event in the phase",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": { "$ref": "log_entry.json" }
            }
          }
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false,
  "required": ["task_id"]
}
"""

###############################################################################
# @Brief: Function to get activity_discovery_response json schema
# @return: json schema, in raw string
def activity_discovery_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/activity_discovery_response.json",
  "title": "Activity Discovery",
  "description": "Discovered information about what kinds of activities a fleet supports",
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "fleet_name": {
            "description": "Name of the fleet that supports these activities",
            "type": "string"
          },
          "activities": {
            "description": "List of activities that the fleet supports",
            "type": "array",
            "items": { "$ref": "#/$defs/activity" }
          }
        },
        "required": ["fleet_name", "activities"]
      }
    }
  },
  "$defs": {
    "activity": {
      "description": "Information about an activity",
      "type": "object",
      "properties": {
        "category": {
          "description": "The category of this activity. There must not be any duplicate activity categories per fleet.",
          "type": "string"
        },
        "detail": {
          "description": "Details about the behavior of the activity.",
          "type": "string"
        },
        "description_schema": {
          "description": "The schema for this activity description",
          "type": "object"
        }
      },
      "required": ["category", "detail", "schema"]
    }
  }
}
"""

###############################################################################
# @Brief: Function to get task_state json schema
# @return: json schema, in raw string
def task_state():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_state.json",
  "title": "Task State",
  "description": "The state of a task",
  "type": "object",
  "properties": {
    "booking": { "$ref": "#/$defs/booking" },
    "category": { "$ref": "#/$defs/category" },
    "detail": { "$ref": "#/$defs/detail" },
    "unix_millis_start_time": { "type": "integer" },
    "unix_millis_finish_time": { "type": "integer" },
    "original_estimate_millis": { "$ref": "#/$defs/estimate_millis" },
    "estimate_millis": { "$ref": "#/$defs/estimate_millis" },
    "assigned_to": {
      "description": "Which agent (robot) is the task assigned to",
      "type": "object",
      "properties": {
        "group": { "type": "string" },
        "name": { "type": "string" }
      },
      "required": ["group", "name"]
    },
    "status": { "$ref": "#/$defs/status" },
    "dispatch": { "$ref": "#/$defs/dispatch" },
    "phases": {
      "description": "A dictionary of the states of the phases of the task. The keys (property names) are phase IDs, which are integers.",
      "type": "object",
      "additionalProperties": { "$ref": "#/$defs/phase" }
    },
    "completed": {
      "description": "An array of the IDs of completed phases of this task",
      "type": "array",
      "items": { "$ref": "#/$defs/id" }
    },
    "active": {
      "description": "The ID of the active phase for this task",
      "$ref": "#/$defs/id"
    },
    "pending": {
      "description": "An array of the pending phases of this task",
      "type": "array",
      "items": { "$ref": "#/$defs/id" }
    },
    "interruptions": {
      "description": "A dictionary of interruptions that have been applied to this task. The keys (property names) are the unique token of the interruption request.",
      "type": "object",
      "additionalProperties": { "$ref": "#/$defs/interruption" }
    },
    "cancellation": {
      "description": "If the task was cancelled, this will describe information about the request.",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the cancellation request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the cancel request",
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    },
    "killed": {
      "description": "If the task was killed, this will describe information about the request.",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the cancellation request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the kill request",
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    }
  },
  "required": ["booking"],
  "$defs": {
    "phase": {
      "description": "Information about a phase",
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/id" },
        "category": { "$ref": "#/$defs/category" },
        "detail": { "$ref": "#/$defs/detail" },
        "unix_millis_start_time": { "type": "integer" },
        "unix_millis_finish_time": { "type": "integer" },
        "original_estimate_millis": { "$ref": "#/$defs/estimate_millis" },
        "estimate_millis": { "$ref": "#/$defs/estimate_millis" },
        "final_event_id": { "$ref": "#/$defs/id" },
        "events": {
          "description": "A dictionary of events for this phase. The keys (property names) are the event IDs, which are integers.",
          "type": "object",
          "additionalProperties": { "$ref": "#/$defs/event_state" }
        },
        "skip_requests": {
          "description": "Information about any skip requests that have been received",
          "type": "object",
          "additionalProperties": { "$ref": "#/$defs/skip_phase_request" }
        }
      },
      "required": ["id"]
    },
    "booking": {
      "description": "Information about how a task was booked",
      "type": "object",
      "properties": {
        "id": {
          "description": "The unique identifier for this task",
          "type": "string"
        },
        "unix_millis_earliest_start_time": { "type": "integer" },
        "priority": {
          "description": "Priority information about this task",
          "anyOf": [
            { "type": "object" },
            { "type": "string" }
          ]
        },
        "labels": {
          "description": "Information about how and why this task was booked",
          "type": "array",
          "items": { "type": "string" }
        }
      },
      "required": ["id"]
    },
    "id": {
      "type": "integer",
      "minimum": 0
    },
    "category": {
      "description": "The category of this task or phase",
      "type": "string"
    },
    "detail": {
      "description": "Detailed information about a task, phase, or event",
      "anyOf": [
        { "type": "object" },
        { "type": "array" },
        { "type": "string" }
      ]
    },
    "estimate_millis": {
      "description": "An estimate, in milliseconds, of how long the subject will take to complete",
      "type": "integer",
      "minimum": 0
    },
    "event_state": {
      "description": "The current state of an event",
      "type": "object",
      "properties": {
        "id": { "$ref": "#/$defs/id" },
        "status": { "$ref": "#/$defs/status"},
        "name": {
          "description": "The brief name of the event",
          "type": "string"
        },
        "detail": {
          "description": "Detailed information about the event",
          "$ref": "#/$defs/detail"
        },
        "deps": {
          "description": "This event may depend on other events. This array contains the IDs of those other event dependencies.",
          "type": "array",
          "items": {
            "description": "The IDs of events that this event depends on. Event IDs are isolated within the scope of this task phase.",
            "type": "integer",
            "minimum": 0
          }
        }
      },
      "required": ["id"]
    },
    "status": {
      "description": "A simple token representing how the task is proceeding",
      "type": "string",
      "enum": ["uninitialized", "blocked", "error", "failed", "queued", "standby", "underway", "delayed", "skipped", "canceled", "killed", "completed"]
    },
    "dispatch": {
      "description": "Information about how this task is being dispatched",
      "type": "object",
      "properties": {
        "status": {
          "type": "string",
          "enum": ["queued", "selected", "dispatched", "failed_to_assign", "canceled_in_flight"]
        },
        "assignment": {
          "type": "object",
          "properties": {
            "fleet_name": { "type": "string" },
            "expected_robot_name": { "type": "string" }
          }
        },
        "errors": {
          "type": "array",
          "items": { "$ref": "error.json" }
        }
      },
      "required": ["status"]
    },
    "interruption": {
      "description": "Task interruption information",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the interruption request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the purpose of the interruption",
          "type": "array",
          "items": { "type": "string" }
        },
        "resumed_by": {
          "description": "Information about the resume request that ended this interruption. This field will be missing if the interruption is still active.",
          "type": "object",
          "properties": {
            "unix_millis_request_time": {
              "description": "The time that the resume request arrived",
              "type": "integer"
            },
            "labels": {
              "description": "Labels to describe the resume request",
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["unix_millis_resume_time", "labels"]
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    },
    "skip_phase_request": {
      "description": "Information about a request to skip a phase",
      "type": "object",
      "properties": {
        "unix_millis_request_time": {
          "description": "The time that the skip request arrived",
          "type": "integer"
        },
        "labels": {
          "description": "Labels to describe the purpose of the skip request",
          "type": "array",
          "items": { "type": "string" }
        },
        "undo": {
          "description": "Information about an undo skip request that applied to this request",
          "type": "object",
          "properties": {
            "unix_millis_request_time": {
              "description": "The time that the undo skip request arrived",
              "type": "integer"
            },
            "labels": {
              "description": "Labels to describe the undo skip request",
              "type": "array",
              "items": { "type": "string" }
            }
          },
          "required": ["unix_millis_request_time", "labels"]
        }
      },
      "required": ["unix_millis_request_time", "labels"]
    }
  }
}
"""

###############################################################################
# @Brief: Function to get task_discovery_request json schema
# @return: json schema, in raw string
def task_discovery_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_discovery_request.json",
  "title": "Task Discovery Request",
  "description": "Ask for tasks that can be performed by the fleets",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task discovery request",
      "type": "string",
      "enum": ["task_discovery_request"]
    }
  },
  "required": ["type"]
}
"""

###############################################################################
# @Brief: Function to get resume_task_request json schema
# @return: json schema, in raw string
def resume_task_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/resume_task_request.json",
  "title": "Task Resume Request",
  "description": "This can be used to discard task interruption requests. When all interruption requests for a task are discarded, the task will resume.",
  "properties": {
    "type": {
      "description": "Indicate that this is a task resuming request",
      "type": "string",
      "enum": ["resume_task_request"]
    },
    "for_task": {
      "description": "Specify task ID to resume.",
      "type": "string"
    },
    "for_tokens": {
      "description": "A list of tokens of interruption requests which should be resumed. The interruption request associated with each token will be discarded.",
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1,
      "uniqueItems": true
    },
    "labels": {
      "description": "Labels describing this request",
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "require": ["type", "for_task", "for_tokens"]
}
"""

###############################################################################
# @Brief: Function to get location_2D json schema
# @return: json schema, in raw string
def location_2D():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/location_2D.json",
  "title": "Location 2D",
  "description": "A robot's location using 2D coordinates",
  "type": "object",
  "properties": {
    "map": { "type": "string" },
    "x": { "type": "number" },
    "y": { "type": "number" },
    "yaw": { "type": "number" }
  },
  "required": ["map", "x", "y", "yaw"]
}
"""

###############################################################################
# @Brief: Function to get undo_skip_phase_request json schema
# @return: json schema, in raw string
def undo_skip_phase_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/undo_phase_skip_request.json",
  "title": "Undo Phase Skip Request",
  "description": "This can be used to discard phase skip requests. When all phase skip requests for a phase are discarded, the phase will not be skipped.",
  "properties": {
    "type": {
      "description": "Indicate that this is a request to undo a phase skip request",
      "type": "string",
      "enum": ["undo_phase_skip_request"]
    },
    "for_task": {
      "description": "Specify the relevant task ID",
      "type": "string"
    },
    "for_tokens": {
      "description": "A list of the tokens of skip requests which should be undone. The skips associated with each token will be discarded.",
      "type": "array",
      "items": { "type": "string" },
      "minItems": 1,
      "uniqueItems": true
    },
    "labels": {
      "description": "Labels describing this request",
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "require": ["type", "for_task", "for_tokens"]
}
"""

###############################################################################
# @Brief: Function to get fleet_log_response json schema
# @return: json schema, in raw string
def fleet_log_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/fleet_log_response.json",
  "title": "Fleet Log Response",
  "description": "Responding to a fleet log request",
  "type": "object",
  "oneOf": [
    {
      "properties": {
        "success": { "$ref": "#/$defs/success" },
        "data": { "$ref": "fleet_log.json" }
      },
      "required": ["success", "data"]
    },
    {
      "properties": {
        "success": { "$ref": "#/$defs/failure" },
        "errors": {
          "description": "Any error messages explaining why the request failed",
          "type": "array",
          "items": { "$ref": "error.json" }
        }
      },
      "required": ["success", "errors"]
    }
  ],
  "$defs": {
    "success": {
      "description": "The request was successful",
      "type": "boolean",
      "enum": [true]
    },
    "failure": {
      "description": "The request failed",
      "type": "boolean",
      "enum": [false]
    }
  }
}
"""

###############################################################################
# @Brief: Function to get kill_task_request json schema
# @return: json schema, in raw string
def kill_task_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/kill_task_request.json",
  "title": "Task Kill Request",
  "description": "Ask for a task to be killed. This should be a last resort if a task cancel request is inadequate.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task kill request",
      "type": "string",
      "enum": ["kill_task_request"]
    },
    "task_id": {
      "description": "Specify the task ID to kill",
      "type": "string"
    },
    "labels": {
      "description": "Labels to describe the purpose of the kill",
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["type", "task_id"]
}
"""

###############################################################################
# @Brief: Function to get simple_response json schema
# @return: json schema, in raw string
def simple_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/simple_response.json",
  "title": "Simple Response",
  "description": "Template for defining a response message that only indicates success and describes any errors",
  "type": "object",
  "oneOf": [
    {
      "properties": {
        "success": { "$ref": "#/$defs/success" }
      },
      "required": ["success"]
    },
    {
      "properties": {
        "success": { "$ref": "#/$defs/failure" },
        "errors": {
          "description": "If the request failed, these error messages will explain why",
          "type": "array",
          "items": { "$ref": "error.json" }
        }
      },
      "required": ["success", "errors"]
    }
  ],
  "$defs": {
    "success": {
      "description": "The request was successful",
      "type": "boolean",
      "enum": [true]
    },
    "failure": {
      "description": "The request failed",
      "type": "boolean",
      "enum": [false]
    }
  }
}
"""

###############################################################################
# @Brief: Function to get task_state_update json schema
# @return: json schema, in raw string
def task_state_update():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_state_update.json",
  "title": "Task State Update",
  "description": "Update for the state of a fleet",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a task state update",
      "type": "string",
      "enum": ["task_state_update"]
    },
    "data": {
      "$ref": "task_state.json"
    }
  },
  "required": ["type", "data"]
}
"""

###############################################################################
# @Brief: Function to get skip_phase_request json schema
# @return: json schema, in raw string
def skip_phase_request():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/skip_phase_request.json",
  "title": "Task Phase Skip Request",
  "description": "Ask for a phase to be skipped.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a phase skip request",
      "type": "string",
      "enum": ["skip_phase_request"]
    },
    "task_id": {
      "description": "Specify the task ID whose phase should be skipped",
      "type": "string"
    },
    "phase_id": {
      "description": "Specify the phase that should be skipped",
      "type": "integer",
      "minimum": 0
    },
    "labels": {
      "description": "Labels to describe the purpose of the skip",
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["type", "task_id", "phase_id"]
}
"""

###############################################################################
# @Brief: Function to get task_log_response json schema
# @return: json schema, in raw string
def task_log_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/task_log_response.json",
  "title": "Task Log Response",
  "description": "Responding to a task log request",
  "type": "object",
  "oneOf": [
    {
      "properties": {
        "success": { "$ref": "#/$defs/success" },
        "data": { "$ref": "task_log.json" }
      },
      "required": ["success", "data"]
    },
    {
      "properties": {
        "success": { "$ref": "#/$defs/failure" },
        "errors": {
          "description": "Any error messages explaining why the request failed",
          "type": "array",
          "items": { "$ref": "error.json" }
        }
      },
      "required": ["success", "errors"]
    }
  ],
  "$defs": {
    "success": {
      "description": "The request was successful",
      "type": "boolean",
      "enum": [true]
    },
    "failure": {
      "description": "The request failed",
      "type": "boolean",
      "enum": [false]
    }
  }
}
"""

###############################################################################
# @Brief: Function to get resume_task_response json schema
# @return: json schema, in raw string
def resume_task_response():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/resume_task_response.json",
  "title": "Task Resume Response",
  "description": "Response to a request to resume a task",
  "$ref": "simple_response.json"
}
"""

###############################################################################
# @Brief: Function to get fleet_log_update json schema
# @return: json schema, in raw string
def fleet_log_update():
    return r"""
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/fleet_log_update.json",
  "title": "Task Event Log Update",
  "description": "Update for the log of a task. These new entries should be appended to any log entries that already existed for the fleet, ignoring any with a duplicate `seq` value.",
  "type": "object",
  "properties": {
    "type": {
      "description": "Indicate that this is a fleet log update",
      "type": "string",
      "enum": ["fleet_log_update"]
    },
    "data": {"$ref": "fleet_log.json" }
  },
  "required": ["type", "data"]
}
"""

