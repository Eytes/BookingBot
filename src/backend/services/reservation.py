from pydantic import BaseModel

from ..base_types import ItemId
from ..repositories.reservation import ReservationRepository
from ..schemas.reservation import (
    CreateReservationSchema,
    UpdateReservationSchema,
    ReservationSchema,
)


class ReservationService:
    def __init__(self, repository) -> None:
        self.__repository = repository

    async def create(self, reservation: CreateReservationSchema) -> ReservationSchema:
        return ReservationRepository.create(reservation)

    async def update(
        self, reservation_id: ItemId, new_data: UpdateReservationSchema
    ) -> ReservationSchema:
        return ReservationRepository.update(reservation_id, new_data)

    async def get_all(self) -> BaseModel or str:
        res = ReservationRepository.get_all()
        if res != None:
            return res
        else:
            return "Бронирований нет"

    async def get_by_id(self, reservation_id: ItemId) -> BaseModel or str:
        res = ReservationRepository.get_one(reservation_id)
        if res != None:
            return res
        else:
            return "Бронирование по этому айди не был найден"

    async def get_by_start_time(
        self, reservation_start_time: ReservationSchema.since_datetime
    ) -> BaseModel or str:
        res = ReservationRepository.get_by_start_time(reservation_start_time)
        if res != None:
            return res
        else:
            return "Бронирование по этому времени не был найден"

    async def get_by_end_time(
        self, reservation_end_time: ReservationSchema.until_datetime
    ) -> BaseModel or str:
        res = ReservationRepository.get_by_end_time(reservation_end_time)
        if res != None:
            return res
        else:
            return "Бронирование по этому айди не был найден"

    async def delete_by_id(self, reservation_id: ItemId) -> BaseModel or str:
        res = ReservationRepository.delete_one(reservation_id)
        if res != None:
            return res
        else:
            return "Бронирование по этому айди не был найден"
