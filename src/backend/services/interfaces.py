from abc import ABC, abstractmethod

from ..types import ObjectId


class GetByIdInterface(ABC):
    @abstractmethod
    async def get_by_id(self, object_id: type[ObjectId]) -> ObjectId:
        pass
