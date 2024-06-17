from typing import TypeAlias, Annotated
from uuid import UUID

from pydantic_extra_types import phone_numbers

ItemId: TypeAlias = Annotated[str, UUID.hex]
PhoneType: phone_numbers
