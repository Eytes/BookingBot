from pydantic import BaseModel

from ..base_types import ItemId


class UserBaseSchema(BaseModel):
    surname: str
    name: str


class UserSchema(UserBaseSchema, ItemId):
    pass


class UserCreateSchema(UserSchema):
    pass
