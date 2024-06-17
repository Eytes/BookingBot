from datetime import datetime

from pydantic import BaseModel

from .mixins import MixinId
from ..base_types import ItemId


class ReservationBaseSchema(BaseModel):
    since_datetime: datetime
    until_datetime: datetime
    audience_id: ItemId
    user_id: ItemId | None


class ReservationSchema(ReservationBaseSchema, MixinId):
    pass


class UpdateReservationSchema(ReservationSchema):
    pass


class CreateReservationSchema(ReservationSchema):
    pass
