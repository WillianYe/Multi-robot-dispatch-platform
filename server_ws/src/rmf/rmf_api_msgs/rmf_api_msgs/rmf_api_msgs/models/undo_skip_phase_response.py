# generated by datamodel-codegen:
#   filename:  undo_skip_phase_response.json

from __future__ import annotations

from pydantic import BaseModel, Field

from . import simple_response


class UndoPhaseSkipResponse(BaseModel):
    __root__: simple_response.SimpleResponse = Field(
        ...,
        description='Response to an undo phase skip request',
        title='Undo Phase Skip Response',
    )
