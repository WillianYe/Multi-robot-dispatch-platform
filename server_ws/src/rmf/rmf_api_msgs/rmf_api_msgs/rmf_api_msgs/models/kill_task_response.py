# generated by datamodel-codegen:
#   filename:  kill_task_response.json

from __future__ import annotations

from pydantic import BaseModel, Field

from . import simple_response


class TaskKillResponse(BaseModel):
    __root__: simple_response.SimpleResponse = Field(
        ...,
        description='Response to a request to kill a task',
        title='Task Kill Response',
    )
