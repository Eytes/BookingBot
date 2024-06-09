from datetime import datetime

from pydantic import BaseModel

from mixins import MixinId
from ..base_types import ItemId


class ReservationBaseSchema(BaseModel):
    reservation_id: ItemId
    since_datetime: datetime
    until_datetime: datetime


class ReservationSchema(ReservationBaseSchema, MixinId):
    pass


class UpdateReservationSchema(ReservationSchema):
    pass


class CreateReservationSchema(ReservationSchema):
    pass
