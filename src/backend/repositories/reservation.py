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
        return await reservation_collection.insert_one(
            {
                "id": reservation.id,
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
        """Обновляет существующую запись о бронировании в базе данных."""
        return await reservation_collection.find_one_and_update(
            {"id": reservation_id},
            {
                "$set": {
                    "since_datetime": new_data.since_datetime,
                    "until_datetime": new_data.until_datetime,
                }
            },
        )

    @classmethod
    async def get_all(cls) -> list[ReservationSchema]:
        """Возвращает список всех записей о бронированиях из базы данных."""
        return list(await reservation_collection.find())

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
