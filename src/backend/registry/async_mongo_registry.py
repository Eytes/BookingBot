from abc import ABC
from typing import Sequence

from motor.motor_asyncio import AsyncIOMotorCollection

from ..base_types import ItemId, Schema


class AsyncMongoRegistry(ABC):
    def __init__(self, collection: AsyncIOMotorCollection) -> None:
        self.__collection = collection

    async def get_by_id(self, item_id: ItemId) -> Sequence[Schema]:
        pass

    async def create(self, new_item: Schema) -> ItemId:
        pass

    async def delete_by_id(self, item_id: ItemId) -> ItemId:
        pass
