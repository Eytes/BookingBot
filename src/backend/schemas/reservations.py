from datetime import time, datetime

from mixins import MixinId
from ..base_types import ItemId, Schema


class ReservationBaseSchema(Schema):
    user_id: ItemId
    audience_id: ItemId
    since_time: datetime
    until_time: datetime


class ReservationSchema(ReservationBaseSchema, MixinId):
    pass


class CreateBookingFacilitiesSchema(ReservationSchema):
    pass
