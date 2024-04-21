from datetime import time, datetime

from mixins import MixinId
from ..base_types import ItemId, Schema


class AudienceBaseSchema(Schema):
    capacity: int
    description: str


class AudienceSchema(Schema, AudienceBaseSchema, MixinId):
    pass


class CreateAudienceSchema(Schema, AudienceSchema):
    pass
