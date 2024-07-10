# generated by datamodel-codegen:
#   filename:  fleet_state_update.json

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from . import fleet_state


class Type5(Enum):
    fleet_state_update = 'fleet_state_update'


class FleetStateUpdate(BaseModel):
    type: Type5 = Field(..., description='Indicate that this is a fleet state update')
    data: fleet_state.FleetState