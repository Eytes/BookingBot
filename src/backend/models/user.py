from pydantic import BaseModel

from ..base_types import ItemId


class UserBaseModel(BaseModel):
    tg_id: ItemId
    nickname: str
