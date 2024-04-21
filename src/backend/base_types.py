from typing import TypeVar, TypeAlias, Annotated
from uuid import UUID

from pydantic import BaseModel

ItemId: TypeAlias = Annotated[str, UUID.hex]
Schema = TypeVar("Schema", bound=BaseModel)
