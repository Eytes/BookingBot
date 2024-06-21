from pydantic import BaseModel

from backend.base_types import PhoneType
from backend.schemas.mixins import MixinId


class UserBaseSchema(BaseModel):
    surname: str
    name: str
    phone_number: PhoneType


class UserSchema(UserBaseSchema, MixinId):
    pass


class CreateUserSchema(UserSchema):
    pass
