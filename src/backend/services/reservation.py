from pydantic import BaseModel

from catcher_of_errors import Not_found
from ..base_types import ItemId
from ..repositories.reservation import reservation_repository
from ..schemas.reservation import (
    CreateReservationSchema,
    UpdateReservationSchema,
    ReservationSchema,
)


class ReservationService:
    def __init__(self, repository) -> None:
        self.__repository = repository

    async def create(self, reservation: CreateReservationSchema) -> ReservationSchema:
        return reservation_repository.create(reservation)

    async def update(
        self, reservation_id: ItemId, new_data: UpdateReservationSchema
    ) -> ReservationSchema:
        return reservation_repository.update(reservation_id, new_data)

    async def get_all(self) -> BaseModel or str:
        return Not_found(reservation_repository.get_all(), "Бронирований нет")

    async def get_by_id(self, reservation_id: ItemId) -> BaseModel or str:
        return Not_found(
            reservation_repository.get_one(reservation_id),
            "Бронирование по этому айди не был найден",
        )

    async def get_by_start_time(
        self, reservation_start_time: ReservationSchema.since_datetime
    ) -> BaseModel or str:
        return Not_found(
            reservation_repository.get_by_start_time(reservation_start_time),
            "Бронирование по этому времени не был найден",
        )

    async def get_by_end_time(
        self, reservation_end_time: ReservationSchema.until_datetime
    ) -> BaseModel or str:
        return Not_found(
            reservation_repository.get_by_end_time(reservation_end_time),
            "Бронирование по этому времени не был найден",
        )

    async def delete_by_id(self, reservation_id: ItemId) -> BaseModel or str:
        res = reservation_repository.delete_one(reservation_id)
        return Not_found(
            reservation_repository.delete_one(reservation_id),
            "Бронирование по этому времени не был найден",
        )
