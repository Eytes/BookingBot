from ..base_types import ItemId
from ..registry import AsyncRegistry, AsyncDBHelper
from ..schemas.user import UserSchema, CreateUserSchema


class UserService:
    def __init__(self, registry: AsyncRegistry, db_helper: AsyncDBHelper) -> None:
        self.__registry = registry
        self.__db_helper = db_helper

    async def get_by_id(self, user_id: ItemId) -> UserSchema: ...

    async def create(self, new_user: CreateUserSchema) -> UserSchema: ...

    async def delete_by_id(self, user_id: ItemId) -> UserSchema: ...
