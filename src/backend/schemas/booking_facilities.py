from datetime import time, datetime

from mixins import MixinId
from ..base_types import ItemId, Schema


class BookingFacilitiesBaseSchema(Schema):
    user_id: ItemId
    audience_id: ItemId
    since_time: time
    until_time: time
    date: datetime


class BookingFacilitiesSchema(Schema, BookingFacilitiesBaseSchema, MixinId):
    pass

class CreateBookingFacilitiesSchema(Schema,BookingFacilitiesSchema):
    pass

