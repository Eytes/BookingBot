import asyncio
from typing import Any, Mapping

from motor.motor_asyncio import (
    AsyncIOMotorCollection,
    AsyncIOMotorClientSession,
    AsyncIOMotorDatabase,
)

from . import mongo_helper
from ..base_types import ItemId, Schema


class AsyncMongoRegistry:
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.__collection = collection

    async def get_by_id(self, item_id: ItemId) -> Mapping[str, Any] | None:
        """Получить запись из БД по id"""
        return await self.__collection.find_one({"_id": item_id})

    async def create(
        self,
        document: Schema,
        session: AsyncIOMotorClientSession,
    ) -> ItemId:
        """Создание записи в БД"""
        result = await self.__collection.insert_one(
            document=document.model_dump(),
            session=session,
        )
        return result.inserted_id

    async def delete_by_id(
        self,
        item_id: ItemId,
        session: AsyncIOMotorClientSession,
    ) -> Mapping[str, Any]:
        """Удаление записи из БД. Возвращается сама запись, которая была удалена"""
        return await self.__collection.find_one_and_delete(
            {"_id": item_id},
            session=session,
        )


class AsyncMongoRegistryFactory:
    def __init__(self, database: AsyncIOMotorDatabase = mongo_helper.database):
        self.__database = database

    def __get_collection_names(self) -> list[str]:
        return asyncio.run(self.__database.list_collection_names())

    def __check_collection_name(self, collection_name: str) -> None:
        if collection_name not in self.__get_collection_names():
            raise ValueError("Коллекция не существует")

    def get_registry(self, collection_name: str) -> AsyncMongoRegistry:
        self.__check_collection_name(collection_name)
        return AsyncMongoRegistry(self.__database[collection_name])
