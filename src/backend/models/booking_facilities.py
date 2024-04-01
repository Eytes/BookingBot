from pydantic import BaseModel

from ..base_types import ItemId


class BookingFacilitiesBaseModel(BaseModel):
    id: ItemId
    title: str
