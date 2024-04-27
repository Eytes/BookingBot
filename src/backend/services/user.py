from ..registry import AsyncRegistry, AsyncDBHelper


class UserService:
    def __init__(self, registry: AsyncRegistry, db_helper: AsyncDBHelper) -> None:
        self.__registry = registry
        self.__db_helper = db_helper
