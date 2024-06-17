from pymongo.results import InsertOneResult

from . import reservation_collection
from ..base_types import ItemId
from ..schemas.reservation import (
    CreateReservationSchema,
    ReservationSchema,
    UpdateReservationSchema,
)


class ReservationRepository:
    @classmethod
    def create(cls, reservation: CreateReservationSchema) -> InsertOneResult:
        return reservation_collection.insert_one(
            {
                "id": reservation.id,
                "since_datetime": reservation.since_datetime,
                "until_datetime": reservation.until_datetime,
            }
        )

    @classmethod
    def update(
        cls,
        reservation_id: ItemId,
        new_data: UpdateReservationSchema,
    ) -> ReservationSchema:
        return reservation_collection.find_one_and_update(
            {"id": reservation_id},
            {
                "$set": {
                    "since_datetime": new_data.since_datetime,
                    "until_datetime": new_data.until_datetime,
                }
            },
        )

    @classmethod
    def get_all(cls) -> list[ReservationSchema]:
        return list(reservation_collection.find())

    @classmethod
    def get_one(
        cls,
        reservation_id: ItemId,
    ) -> ReservationSchema:
        return reservation_collection.find_one({"id": reservation_id})

    @classmethod
    def delete_one(
        cls,
        reservation_id: ItemId,
    ) -> ReservationSchema:
        return reservation_collection.find_one_and_delete({"id": reservation_id})
