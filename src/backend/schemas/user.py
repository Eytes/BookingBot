from pydantic import BaseModel

from ..base_types import ItemId


class __UserBaseSchema(BaseModel):
    nickname: str


class UserSchema(__UserBaseSchema):
    tg_id: ItemId


class CreateUserSchema(UserSchema):
    pass
