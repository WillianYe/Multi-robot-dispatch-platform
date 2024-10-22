# generated by datamodel-codegen:
#   filename:  skip_phase_response.json

from __future__ import annotations

from pydantic import BaseModel, Field

from . import token_response


class SkipPhaseResponse(BaseModel):
    __root__: token_response.TokenResponse = Field(
        ...,
        description='Response to a request for a phase to be skipped',
        title='Skip Phase Response',
    )
