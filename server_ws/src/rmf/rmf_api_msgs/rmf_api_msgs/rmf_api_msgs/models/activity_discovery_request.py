# generated by datamodel-codegen:
#   filename:  activity_discovery_request.json

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class Type8(Enum):
    activitiy_discovery_request = 'activitiy_discovery_request'


class ActivityDiscoveryRequest(BaseModel):
    type: Type8 = Field(
        ..., description='Indicate that this is an activity discovery request'
    )
