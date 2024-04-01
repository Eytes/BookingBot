from pydantic import BaseModel

from ..base_types import ItemId


class UserSchema(BaseModel):
    tg_id: ItemId
    nickname: str
