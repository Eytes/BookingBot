from abc import ABC, abstractmethod

from ..base_types import ItemId, Schema


class GetByIdInterface(ABC):
    @abstractmethod
    async def get_by_id(self, item_id: ItemId) -> Schema:
        pass


class DeleteByIdInterface(ABC):
    @abstractmethod
    async def delete_by_id(self, item_id: ItemId) -> None:
        pass
