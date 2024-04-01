from pydantic import BaseModel

from ..base_types import ItemId


class BookingFacilitiesSchema(BaseModel):
    id: ItemId
    title: str
