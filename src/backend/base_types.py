from typing import TypeAlias, Annotated
from uuid import UUID

from pydantic_extra_types.phone_numbers import PhoneNumber

ItemId: TypeAlias = Annotated[str, UUID.hex]
PhoneType: PhoneNumber
