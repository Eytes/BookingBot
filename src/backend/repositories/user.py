from . import user_collection, reservation_collection
from ..base_types import ItemId
from ..schemas.user import (
    CreateUserSchema,
    UserSchema,
)


class UserRepository:
    """
    Репозиторий для работы с записями о пользователях в базе данных.
    """

    @classmethod
    async def create(cls, user: CreateUserSchema) -> UserSchema:
        """Создает новую запись о пользователе в базе данных."""
        return await user_collection.insert_one(
            {
                "id": user.id,
                "capacity": user.capacity,
                "description": user.description,
            }
        )

    @classmethod
    async def get_all(cls) -> list[UserSchema]:
        """Возвращает список всех записей о пользователях из базы данных."""
        return list(await user_collection.find())

    @classmethod
    async def get_one(
        cls,
        user_id: ItemId,
    ) -> UserSchema:
        """Получить запись о пользователе из базы данных по id."""
        return await user_collection.find_one({"id": user_id})

    @classmethod
    async def get_by_reservation(
        cls,
        reservation_id: ItemId,
    ) -> UserSchema:
        """Возвращает запись о пользователе, связанного с указанным бронированием."""
        return await user_collection.find_one(
            {"id": reservation_collection.find_one({"id": reservation_id}).user_id}
        )

    @classmethod
    async def delete_one(
        cls,
        user_id: ItemId,
    ) -> UserSchema:
        """Удаляет запись о пользователе из базы данных по id."""
        return await user_collection.find_one_and_delete({"id": user_id})


user_repository = UserRepository
