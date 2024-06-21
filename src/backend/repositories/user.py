from pymongo.results import InsertOneResult

from . import user_collection
from ..base_types import ItemId
from ..schemas.user import (
    CreateUserSchema,
    UserSchema,
)


class UserRepository:
    @classmethod
    def create(cls, user: CreateUserSchema) -> InsertOneResult:
        return user_collection.insert_one(
            {
                "id": user.id,
                "capacity": user.capacity,
                "description": user.description,
            }
        )

    @classmethod
    def get_all(cls) -> list[UserSchema]:
        return list(user_collection.find())

    @classmethod
    def get_one(
        cls,
        user_id: ItemId,
    ) -> UserSchema:
        return user_collection.find_one({"id": user_id})

    @classmethod
    def delete_one(
        cls,
        reservation_id: ItemId,
    ) -> UserSchema:
        return user_collection.find_one_and_delete({"id": reservation_id})
