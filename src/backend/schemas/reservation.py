from datetime import datetime

from pydantic import BaseModel

from .mixins import MixinId


class ReservationBaseSchema(BaseModel):
    since_datetime: datetime
    until_datetime: datetime


class ReservationSchema(ReservationBaseSchema, MixinId):
    pass


class UpdateReservationSchema(ReservationSchema):
    pass


class CreateReservationSchema(ReservationSchema):
    pass
