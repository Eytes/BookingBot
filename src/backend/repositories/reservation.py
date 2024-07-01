import pymongo

from . import reservation_collection
from ..base_types import ItemId
from ..schemas.reservation import (
    CreateReservationSchema,
    ReservationSchema,
    UpdateReservationSchema,
)


class ReservationRepository:
    """
    Репозиторий для работы с записями о бронированиях в базе данных.
    """

    @classmethod
    async def create(cls, reservation: CreateReservationSchema) -> ReservationSchema:
        """Создает новую запись о бронировании в базе данных."""
        return await reservation_collection.insert_one(reservation.model_dump())

    @classmethod
    async def update(
        cls,
        reservation_id: ItemId,
        new_data: UpdateReservationSchema,
    ) -> ReservationSchema:
        """Обновляет существующую запись о бронировании в базе данных."""
        return await reservation_collection.find_one_and_update(
            {"id": reservation_id},
            {"$set": new_data.model_dump()},
        )

    @classmethod
    async def get_all(cls, start_num: int, end_num: int) -> list[ReservationSchema]:
        """Возвращает список записей о бронированиях с какойто до какой-то из базы данных."""
        return list(
            await reservation_collection.find()
            .sort("_id", pymongo.ASCENDING)
            .skip(start_num - 1)
            .limit(end_num - start_num)
            .next()
        )

    @classmethod
    async def get_one(
        cls,
        reservation_id: ItemId,
    ) -> ReservationSchema:
        """Получить запись о бронировании из базы данных по id."""
        return await reservation_collection.find_one({"id": reservation_id})

    @classmethod
    async def get_by_start_time(
        cls, reservation_start_time: ReservationSchema.since_datetime
    ) -> list[ReservationSchema]:
        """Возвращает список записей о бронированиях, начинающихся в указанное время."""
        return await reservation_collection.find_many(
            {"since_datetime": reservation_start_time}
        )

    @classmethod
    async def get_by_end_time(
        cls, reservation_end_time: ReservationSchema.since_datetime
    ) -> list[ReservationSchema]:
        """Возвращает список записей о бронированиях, заканчивающихся в указанное время."""
        return await reservation_collection.find_many(
            {"until_datetime": reservation_end_time}
        )

    @classmethod
    async def delete_one(
        cls,
        reservation_id: ItemId,
    ) -> ReservationSchema:
        """Удаляет запись о бронировании из базы данных по id."""
        return await reservation_collection.find_one_and_delete({"id": reservation_id})


reservation_repository = ReservationRepository
