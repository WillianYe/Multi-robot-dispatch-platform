# generated by datamodel-codegen:
#   filename:  dispatch_task_response.json

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Field

from . import error, task_state


class Success1(Enum):
    boolean_True = True


class Success2(Enum):
    boolean_False = False


class TaskDispatchResponseItem1(BaseModel):
    success: Optional[Success2] = None
    errors: Optional[List[error.Error]] = Field(
        None, description='Any error messages explaining why the request failed'
    )


class TaskDispatchResponseItem(BaseModel):
    success: Success1
    state: task_state.TaskState


class TaskDispatchResponse(BaseModel):
    __root__: Union[TaskDispatchResponseItem, TaskDispatchResponseItem1] = Field(
        ...,
        description='Response to a task dispatch request',
        title='Task Dispatch Response',
    )
