from pydantic import BaseModel

from ..base_types import ItemId


class __BookingFacilitiesBaseSchema(BaseModel):
    title: str


class BookingFacilitiesSchema(__BookingFacilitiesBaseSchema):
    id: ItemId


class CreateBookingFacilitiesSchema(BookingFacilitiesSchema):
    pass
