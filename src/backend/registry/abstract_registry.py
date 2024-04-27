from abc import ABC, abstractmethod
from typing import Any

from ..base_types import ItemId, Schema, T


class AsyncRegistry(ABC):
    @abstractmethod
    async def get_by_id(self, item_id: ItemId) -> list[tuple[str, Any] | None]: ...

    @abstractmethod
    async def create(self, item_data: Schema, session: T) -> ItemId: ...

    @abstractmethod
    async def delete_by_id(
        self,
        item_id: ItemId,
        session: T,
    ) -> list[tuple[str, Any]]: ...
