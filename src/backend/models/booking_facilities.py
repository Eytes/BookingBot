from pydantic import BaseModel

from ..types import ObjectId


class BookingFacilitiesBaseModel(BaseModel):
    id: ObjectId
    title: str
