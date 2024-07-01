from pydantic import BaseModel

from catcher_of_errors import reservation_not_found, result_not_found
from ..base_types import ItemId
from ..repositories.reservation import reservation_repository
from ..schemas.reservation import (
    CreateReservationSchema,
    UpdateReservationSchema,
    ReservationSchema,
)


class ReservationService:
    """
    Сервис для работы с бронированиями.
    """

    def __init__(self, repository) -> None:
        self.__repository = repository

    async def create(self, reservation: CreateReservationSchema) -> ReservationSchema:
        """Создает новое бронирование."""
        return ReservationSchema.parse_obj(
            await reservation_repository.create(reservation)
        )

    async def update(
        self, reservation_id: ItemId, new_data: UpdateReservationSchema or str
    ) -> ReservationSchema:
        """Обновляет существующее бронирование."""
        return result_not_found(
            await reservation_repository.update(reservation_id, new_data),
            reservation_not_found,
        )

    async def get_all(cls, start_num: int, end_num: int) -> BaseModel or str:
        """Возвращает список всех бронирований."""
        return (
            result_not_found(
                await reservation_repository.get_all(abs(start_num), abs(end_num)),
                "Бронирований нет",
            )
            if abs(end_num) > abs(start_num)
            else "Первое значение должно быть меньше чем второе"
        )

    async def get_by_id(self, reservation_id: ItemId) -> BaseModel or str:
        """Возвращает бронирование по его ID."""
        return result_not_found(
            await reservation_repository.get_one(reservation_id),
            reservation_not_found,
        )

    async def get_by_start_time(
        self, reservation_start_time: ReservationSchema.since_datetime
    ) -> BaseModel or str:
        """Возвращает список бронирований, начинающихся в указанное время."""
        return result_not_found(
            await reservation_repository.get_by_start_time(reservation_start_time),
            "Бронирование по этому времени не был найдено",
        )

    async def get_by_end_time(
        self, reservation_end_time: ReservationSchema.until_datetime
    ) -> BaseModel or str:
        """Возвращает список бронирований, заканчивающихся в указанное время."""
        return result_not_found(
            await reservation_repository.get_by_end_time(reservation_end_time),
            "Бронирование по этому времени не было найдено",
        )

    async def delete_by_id(self, reservation_id: ItemId) -> BaseModel or str:
        """Удаляет бронирование по его ID."""
        return result_not_found(
            await reservation_repository.delete_one(reservation_id),
            reservation_not_found,
        )
