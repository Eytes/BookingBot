from pymongo.results import InsertOneResult

from . import audience_collection
from ..base_types import ItemId
from ..schemas.audience import (
    CreateAudienceSchema,
    AudienceSchema,
    UpdateAudienceSchema,
)


class AudienceRepository:
    @classmethod
    def create(cls, audience: CreateAudienceSchema) -> InsertOneResult:
        return audience_collection.insert_one(
            {
                "id": audience.id,
                "capacity": audience.capacity,
                "description": audience.description,
            }
        )

    @classmethod
    def update(
        cls,
        audience_id: ItemId,
        new_data: UpdateAudienceSchema,
    ) -> AudienceSchema:
        return audience_collection.find_one_and_update(
            {"id": audience_id},
            {
                "$set": {
                    "capacity": new_data.capacity,
                    "description": new_data.description,
                }
            },
        )

    @classmethod
    def get_all(cls) -> list[AudienceSchema]:
        return list(audience_collection.find())

    @classmethod
    def get_one(
        cls,
        audience_id: ItemId,
    ) -> AudienceSchema:
        return audience_collection.find_one({"id": audience_id})

    @classmethod
    def delete_one(
        cls,
        reservation_id: ItemId,
    ) -> AudienceSchema:
        return audience_collection.find_one_and_delete({"id": reservation_id})
