from ..registry import AsyncMongoRegistry


class UserService:
    def __init__(self, registry: AsyncMongoRegistry) -> None:
        self.__registry = registry
