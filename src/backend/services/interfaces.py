from abc import ABC, abstractmethod

from ..base_types import ItemId, BaseModel


class GetByIdInterface(ABC):
    @abstractmethod
    async def get_by_id(self, object_id: ItemId) -> BaseModel:
        pass
