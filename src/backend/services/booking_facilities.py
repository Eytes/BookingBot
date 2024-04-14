from ..registry import AsyncMongoRegistry


class BookingFacilitiesService:
    def __init__(self, registry: AsyncMongoRegistry) -> None:
        self.__registry = registry
