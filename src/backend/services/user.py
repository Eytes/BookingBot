from pydantic import BaseModel

from .catcher_of_errors import Not_found, user_not_found, reservation_not_found
from ..base_types import ItemId
from ..repositories.user import user_repository
from ..schemas.user import (
    CreateUserSchema,
    UserSchema,
)


class UserService:
    def __init__(self, repository) -> None:
        self.__repository = repository

    async def create(self, audience: CreateUserSchema) -> UserSchema:
        return user_repository.create(audience)

    async def get_all(self) -> BaseModel or str:
        return Not_found(user_repository.get_all(), "Пользователей нет")

    async def get_by_id(self, audience_id: ItemId) -> BaseModel or str:
        return Not_found(
            user_repository.get_one(audience_id),
            user_not_found,
        )

    async def get_by_reservation_id(self, reservation_id: ItemId) -> BaseModel or str:
        return Not_found(
            user_repository.get_by_reservation(reservation_id),
            reservation_not_found,
        )

    async def delete_by_id(self, audience_id: ItemId) -> BaseModel or str:
        return Not_found(
            user_repository.delete_one(audience_id),
            user_not_found,
        )
