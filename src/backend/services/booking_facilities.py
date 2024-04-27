from ..base_types import ItemId
from ..registry import AsyncRegistry, AsyncDBHelper
from ..schemas.booking_facilities import (
    BookingFacilitiesSchema,
    CreateBookingFacilitiesSchema,
)


class BookingFacilitiesService:
    def __init__(self, registry: AsyncRegistry, db_helper: AsyncDBHelper) -> None:
        self.__registry = registry
        self.__db_helper = db_helper

    async def get_by_id(
        self, booking_facilities_id: ItemId
    ) -> BookingFacilitiesSchema: ...

    async def create(
        self, new_booking_facilities: CreateBookingFacilitiesSchema
    ) -> CreateBookingFacilitiesSchema: ...

    async def delete_by_id(
        self, booking_facilities_id: ItemId
    ) -> BookingFacilitiesSchema: ...
