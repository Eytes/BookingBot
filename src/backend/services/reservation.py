from pydantic import BaseModel

from .interfaces import GetByIdInterface
from ..base_types import ItemId


class ReservationService(GetByIdInterface):
    def __init__(self, repository) -> None:
        self.__repository = repository

    async def get_by_id(self, object_id: ItemId) -> BaseModel:
        pass
