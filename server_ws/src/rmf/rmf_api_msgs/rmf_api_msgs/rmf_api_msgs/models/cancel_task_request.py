# generated by datamodel-codegen:
#   filename:  cancel_task_request.json

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class Type1(Enum):
    cancel_task_request = 'cancel_task_request'


class CancelTaskRequest(BaseModel):
    type: Type1 = Field(
        ..., description='Indicate that this is a task cancellation request'
    )
    task_id: str = Field(..., description='Specify the task ID to cancel')
    labels: Optional[List[str]] = Field(
        None, description='Labels to describe the purpose of the cancellation'
    )
