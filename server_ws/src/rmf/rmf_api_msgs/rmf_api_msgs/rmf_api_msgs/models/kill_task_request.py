# generated by datamodel-codegen:
#   filename:  kill_task_request.json

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Type13(Enum):
    kill_task_request = 'kill_task_request'


class TaskKillRequest(BaseModel):
    type: Type13 = Field(..., description='Indicate that this is a task kill request')
    task_id: str = Field(..., description='Specify the task ID to kill')
    labels: Optional[List[str]] = Field(
        None, description='Labels to describe the purpose of the kill'
    )
