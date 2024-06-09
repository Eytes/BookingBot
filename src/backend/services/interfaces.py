from abc import ABC, abstractmethod

from pydantic import BaseModel

from ..base_types import ItemId


class GetByIdInterface(ABC):
    @abstractmethod
    async def get_by_id(self, object_id: ItemId) -> BaseModel:
        pass
