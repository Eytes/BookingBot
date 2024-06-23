from . import audience_collection
from ..base_types import ItemId
from ..schemas.audience import (
    CreateAudienceSchema,
    AudienceSchema,
    UpdateAudienceSchema,
)


class AudienceRepository:
    """
    Репозиторий для работы с записями о залах (парикмахерских) в базе данных.
    """

    @classmethod
    async def create(cls, audience: CreateAudienceSchema) -> AudienceSchema:
        """Создает новую запись о зале в базе данных."""
        return await audience_collection.insert_one(
            {
                "id": audience.id,
                "capacity": audience.capacity,
                "description": audience.description,
            }
        )

    @classmethod
    async def update(
        cls,
        audience_id: ItemId,
        new_data: UpdateAudienceSchema,
    ) -> AudienceSchema:
        """Обновляет существующую запись о зале в базе данных."""
        return await audience_collection.find_one_and_update(
            {"id": audience_id},
            {
                "$set": {
                    "capacity": new_data.capacity,
                    "description": new_data.description,
                }
            },
        )

    @classmethod
    async def get_all(cls) -> list[AudienceSchema]:
        """Возвращает список всех записей о залах из базы данных."""
        return list(await audience_collection.find())

    @classmethod
    async def get_one(
        cls,
        audience_id: ItemId,
    ) -> AudienceSchema:
        """Получить запись о зале из базы данных по id."""
        return await audience_collection.find_one({"id": audience_id})

    @classmethod
    async def get_by_capacity(
        cls,
        audience_capacity: AudienceSchema.capacity,
    ) -> list[AudienceSchema]:
        """Возвращает список записей о залах с указанной вместимостью."""
        return await audience_collection.find_many({"capacity": audience_capacity})

    @classmethod
    async def delete_one(
        cls,
        reservation_id: ItemId,
    ) -> AudienceSchema:
        """Удаляет запись о зале из базы данных по id."""
        return await audience_collection.find_one_and_delete({"id": reservation_id})


audience_repository = AudienceRepository
