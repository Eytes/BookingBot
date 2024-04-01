from typing import TypeVar

from pydantic import BaseModel

ItemId = TypeVar("ItemId", bound=int)
Schema = TypeVar("Schema", bound=BaseModel)
