from pymongo.results import InsertOneResult

from .mongo import mycol
from ..base_types import ItemId
from ..schemas.audience import (
    CreateAudienceSchema,
    AudienceSchema,
    UpdateAudienceSchema,
)


class AudienceRepository:
    @classmethod
    async def create(cls, audience: CreateAudienceSchema) -> InsertOneResult:
        return mycol.insert_one(
            {"capacity": audience.capacity, "description": audience.description}
        )

    @classmethod
    async def update(
        cls,
        audience_id: ItemId,
        new_data: UpdateAudienceSchema,
    ) -> AudienceSchema:
        return mycol.find_one_and_update(
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
        return mycol.find()

    @classmethod
    async def get_one(
        cls,
        audience_id: ItemId,
    ) -> AudienceSchema:
        return mycol.find_one({"id": audience_id})
