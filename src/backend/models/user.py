from pydantic import BaseModel

from ..types import ObjectId


class UserBaseModel(BaseModel):
    tg_id: ObjectId
    nickname: str
