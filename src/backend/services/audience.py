from pydantic import BaseModel

from .catcher_of_errors import audience_not_found, not_found
from ..repositories.audience import *
from ..repositories.audience import audience_repository
from ..schemas.audience import AudienceSchema, CreateAudienceSchema


class AudienceService:
    """
    Сервис для работы с аудиториями.
    """

    def __init__(self, audience) -> None:
        self.__audience = audience

    async def create(self, audience: CreateAudienceSchema) -> AudienceSchema:
        """Создает новую аудиторию."""
        return AudienceSchema.parse_obj(await audience_repository.create(audience))

    async def update(
        self, audience_id: ItemId, new_data: UpdateAudienceSchema
    ) -> AudienceSchema:
        """Обновляет существующую аудиторию."""
        return AudienceSchema.parse_obj(
            await audience_repository.update(audience_id, new_data)
        )

    async def get_all(self) -> BaseModel or str:
        """Возвращает список всех аудиторий."""
        return not_found(await audience_repository.get_all(), "Аудиторий нет")

    async def get_by_id(self, audience_id: ItemId) -> BaseModel or str:
        """Возвращает аудиторию по ее ID."""
        return not_found(
            await audience_repository.get_one(audience_id),
            audience_not_found,
        )

    async def get_by_capacity(self, audience_id: ItemId) -> BaseModel or str:
        """Возвращает список аудиторий с указанной вместимостью."""
        return not_found(
            await audience_repository.get_by_capacity(audience_id),
            audience_not_found,
        )

    async def delete_by_id(self, audience_id: ItemId) -> BaseModel or str:
        """Удаляет аудиторию по ее ID."""
        return not_found(
            await audience_repository.delete_one(audience_id),
            audience_not_found,
        )
