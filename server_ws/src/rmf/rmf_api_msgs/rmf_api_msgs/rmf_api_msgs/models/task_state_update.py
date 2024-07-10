# generated by datamodel-codegen:
#   filename:  task_state_update.json

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from . import task_state


class Type14(Enum):
    task_state_update = 'task_state_update'


class TaskStateUpdate(BaseModel):
    type: Type14 = Field(..., description='Indicate that this is a task state update')
    data: task_state.TaskState