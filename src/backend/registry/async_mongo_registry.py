from typing import Any

from motor.motor_asyncio import (
    AsyncIOMotorCollection,
    AsyncIOMotorClientSession,
    AsyncIOMotorDatabase,
)

from .abstract_registry import AsyncRegistry
from ..base_types import ItemId, Schema


class AsyncMongoRegistry(AsyncRegistry):
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.__collection = collection

    async def get_by_id(self, item_id: ItemId) -> list[tuple[str, Any] | None]:
        """Получить запись из БД по id"""
        item = await self.__collection.find_one({"_id": item_id})
        if not item:
            return list()
        return list(item.items())

    async def create(
        self,
        item_data: Schema,
        session: AsyncIOMotorClientSession,
    ) -> ItemId:
        """Создание записи в БД"""
        result = await self.__collection.insert_one(
            document=item_data.model_dump(),
            session=session,
        )
        return ItemId(result.inserted_id)

    async def delete_by_id(
        self,
        item_id: ItemId,
        session: AsyncIOMotorClientSession,
    ) -> list[tuple[str, Any]]:
        """Удаление записи из БД. Возвращается сама запись, которая была удалена"""
        return list(
            (
                await self.__collection.find_one_and_delete(
                    {"_id": item_id},
                    session=session,
                )
            ).items()
        )


class AsyncMongoRegistryFactory:
    def __init__(self, database: AsyncIOMotorDatabase):
        self.__database = database

    def get_registry(self, collection_name: str) -> AsyncMongoRegistry:
        return AsyncMongoRegistry(self.__database[collection_name])
