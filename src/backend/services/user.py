from pydantic import BaseModel

from .catcher_of_errors import Not_found, user_not_found, reservation_not_found
from ..base_types import ItemId
from ..repositories.user import user_repository
from ..schemas.user import (
    CreateUserSchema,
    UserSchema,
)


class UserService:
    """
    Сервис для работы с пользователями.
    """

    def init(self, repository) -> None:
        self.__repository = repository

    async def create(self, user: CreateUserSchema) -> UserSchema:
        """Создает нового пользователя."""
        return await UserSchema.parse_obj(user_repository.create(user))

    async def get_all(self) -> BaseModel or str:
        """Возвращает список всех пользователей."""
        return await Not_found(user_repository.get_all(), "Пользователей нет")

    async def get_by_id(self, user_id: ItemId) -> BaseModel or str:
        """Возвращает пользователя по его ID."""
        return await Not_found(
            user_repository.get_one(user_id),
            user_not_found,
        )

    async def get_by_reservation_id(self, reservation_id: ItemId) -> BaseModel or str:
        """Возвращает пользователя, связанного с указанным бронированием."""
        return await Not_found(
            user_repository.get_by_reservation(reservation_id),
            reservation_not_found,
        )

    async def delete_by_id(self, user_id: ItemId) -> BaseModel or str:
        """Удаляет пользователя по его ID."""
        return await Not_found(
            user_repository.delete_one(user_id),
            user_not_found,
        )
