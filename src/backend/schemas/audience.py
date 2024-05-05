from mixins import MixinId
from ..base_types import Schema


class AudienceBaseSchema(Schema):
    capacity: int
    description: str


class AudienceSchema(AudienceBaseSchema, MixinId):
    pass


class CreateAudienceSchema(AudienceSchema):
    pass
