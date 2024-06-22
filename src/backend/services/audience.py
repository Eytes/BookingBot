from pydantic import BaseModel

from .catcher_of_errors import Not_found
from ..repositories.audience import *
from ..repositories.audience import audience_repository
from ..schemas.audience import AudienceSchema, CreateAudienceSchema


class AudienceService:
    def __init__(self, audience) -> None:
        self.__audience = audience

    async def create(self, Audience: CreateAudienceSchema) -> AudienceSchema:
        return audience_repository.create(Audience)

    async def update(
        self, Audience_id: ItemId, new_data: UpdateAudienceSchema
    ) -> AudienceSchema:
        return audience_repository.update(Audience_id, new_data)

    async def get_all(self) -> BaseModel or str:
        return Not_found(audience_repository.get_all(), "Бронирований нет")

    async def get_by_id(self, Audience_id: ItemId) -> BaseModel or str:
        return Not_found(
            audience_repository.get_one(Audience_id),
            "Бронирование по этому айди не был найден",
        )

    async def get_by_id(self, Audience_id: ItemId) -> BaseModel or str:
        return Not_found(
            audience_repository.get_by_capacity(Audience_id),
            "Бронирование по этому айди не был найден",
        )

    async def delete_by_id(self, Audience_id: ItemId) -> BaseModel or str:
        res = audience_repository.delete_one(Audience_id)
        return Not_found(
            audience_repository.delete_one(Audience_id),
            "Бронирование по этому времени не был найден",
        )
