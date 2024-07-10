# generated by datamodel-codegen:
#   filename:  token_response.json

from __future__ import annotations

from enum import Enum
from typing import List, Union

from pydantic import BaseModel, Field

from . import error


class Failure(Enum):
    boolean_False = False


class Success(Enum):
    boolean_True = True


class TokenResponseItem(BaseModel):
    success: Success
    token: str = Field(
        ...,
        description='A token for the request. The value of this token is unique within the scope of this request and can be used by other requests to reference this request.',
    )


class TokenResponseItem1(BaseModel):
    success: Failure
    errors: List[error.Error] = Field(
        ..., description='Any error messages explaining why the request failed.'
    )


class TokenResponse(BaseModel):
    __root__: Union[TokenResponseItem, TokenResponseItem1] = Field(
        ...,
        description='Template for defining a response message that provides a token upon success or errors upon failure',
        title='Token Response',
    )