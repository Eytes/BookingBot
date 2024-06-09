from pymongo.results import InsertOneResult

from .mongo import mycol
from ..base_types import ItemId
from ..schemas.reservation import (
    CreateReservationSchema,
    ReservationSchema,
    UpdateReservationSchema,
)


class ReservationRepository:
    @classmethod
    async def create(cls, reservation: CreateReservationSchema) -> InsertOneResult:
        return mycol.insert_one(
            {
                "reservation_id": reservation.reservation_id,
                "since_datetime": reservation.since_datetime,
                "until_datetime": reservation.until_datetime,
            }
        )

    @classmethod
    async def update(
        cls,
        reservation_id: ItemId,
        new_data: UpdateReservationSchema,
    ) -> ReservationSchema:
        return mycol.find_one_and_update(
            {"id": reservation_id},
            {
                "$set": {
                    "reservation_id": new_data.ItemId,
                    "since_datetime": new_data.datetime,
                    "until_datetime": new_data.datetime,
                }
            },
        )

    @classmethod
    async def get_all(cls) -> list[ReservationSchema]:
        return mycol.find()

    @classmethod
    async def get_one(
        cls,
        reservation_id: ItemId,
    ) -> ReservationSchema:
        return mycol.find_one({"id": reservation_id})
