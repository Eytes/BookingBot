from . import reservation_collection
from ..base_types import ItemId
from ..schemas.reservation import (
    CreateReservationSchema,
    ReservationSchema,
    UpdateReservationSchema,
)


class ReservationRepository:
    @classmethod
    def create(cls, reservation: CreateReservationSchema) -> ReservationSchema:
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
    def get_by_start_time(
        cls, reservation_start_time: ReservationSchema.since_datetime
    ) -> list[ReservationSchema]:
        return reservation_collection.find_many(
            {"since_datetime": reservation_start_time}
        )

    @classmethod
    def get_by_end_time(
        cls, reservation_end_time: ReservationSchema.since_datetime
    ) -> list[ReservationSchema]:
        return reservation_collection.find_many(
            {"until_datetime": reservation_end_time}
        )

    @classmethod
    def delete_one(
        cls,
        reservation_id: ItemId,
    ) -> ReservationSchema:
        return reservation_collection.find_one_and_delete({"id": reservation_id})


reservation_repository = ReservationRepository
