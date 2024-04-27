from typing import TypeVar

from pydantic import BaseModel
from pydantic.types import PositiveInt

ItemId = PositiveInt
Schema = BaseModel
T = TypeVar("T")
