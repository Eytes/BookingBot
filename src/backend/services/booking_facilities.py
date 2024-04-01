from .interfaces import GetByIdInterface
from ..types import ObjectId


class BookingFacilitiesService(GetByIdInterface):
    def __init__(self, registry) -> None:
        self.__registry = registry

    async def get_by_id(self, object_id: type[ObjectId]) -> ObjectId:
        pass
