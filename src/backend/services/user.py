from .interfaces import GetByIdInterface
from ..base_types import ItemId, Schema


class UserService(GetByIdInterface):
    def __init__(self, registry) -> None:
        self.__registry = registry

    async def get_by_id(self, object_id: ItemId) -> Schema:
        pass
