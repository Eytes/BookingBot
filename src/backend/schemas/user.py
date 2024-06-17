from pydantic import BaseModel

from backend.schemas.mixins import MixinId


class UserBaseSchema(BaseModel):
    surname: str
    name: str


class UserSchema(UserBaseSchema, MixinId):
    pass


class UserCreateSchema(UserSchema):
    pass
