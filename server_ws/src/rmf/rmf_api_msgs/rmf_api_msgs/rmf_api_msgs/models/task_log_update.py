# generated by datamodel-codegen:
#   filename:  task_log_update.json

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from . import task_log


class Type9(Enum):
    task_log_update = 'task_log_update'


class TaskEventLogUpdate(BaseModel):
    type: Type9 = Field(..., description='Indicate that this is an event log update')
    data: task_log.TaskEventLog
