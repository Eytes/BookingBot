from typing import AsyncGenerator

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorClientSession,
    AsyncIOMotorDatabase,
)

from ..config import settings


class AsyncMongoHelper:
    def __init__(self, client_url: str, database_name: str) -> None:
        self.__mongo_client = AsyncIOMotorClient(client_url)
        self.__mongo_database = self.__mongo_client[database_name]

    @property
    def client(self) -> AsyncIOMotorClient:
        return self.__mongo_client

    @property
    def database(self) -> AsyncIOMotorDatabase:
        return self.__mongo_database

    async def get_session(self) -> AsyncGenerator[AsyncIOMotorClientSession, None]:
        """Создается новая сессия. После окончания операций автоматически завершается"""
        async with self.client.start_session() as session:
            yield session
            await session.end_session()


mongo_helper = AsyncMongoHelper(
    client_url=settings.mongodb.url,
    database_name=settings.mongodb.database_name,
)