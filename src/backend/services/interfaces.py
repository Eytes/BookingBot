from abc import ABC, abstractmethod

from ..base_types import ItemId, Schema


class GetByIdInterface(ABC):
    @abstractmethod
    async def get_by_id(self, object_id: ItemId) -> Schema:
        pass
