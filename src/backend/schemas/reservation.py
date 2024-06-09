from datetime import time, datetime

from pydantic import BaseModel

from mixins import MixinId
from ..base_types import ItemId


class ReservationBaseSchema(BaseModel):
    user_id: ItemId
    audience_id: ItemId
    since_time: time
    until_time: time
    date: datetime


class ReservationSchema(ReservationBaseSchema, MixinId):
    pass


class CreateReservationSchema(ReservationSchema):
    pass
