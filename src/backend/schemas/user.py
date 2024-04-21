from ..base_types import ItemId, Schema


class UserBaseSchema(Schema):
    surname: str
    name: str


class UserSchema(Schema, UserBaseSchema):
    tg_id: ItemId


class UserCreate(UserSchema):
    pass
