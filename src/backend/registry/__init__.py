from motor.motor_asyncio import AsyncIOMotorClient

from .async_mongo_registry import AsyncMongoRegistry
from ..config import settings

__mongo_client = AsyncIOMotorClient(settings.mongodb.url)
__mongo_database = __mongo_client[settings.mongodb.database_name]

UserMongoRegistry = AsyncMongoRegistry(__mongo_database["users"])
BookingFacilitiesMongoRegistry = AsyncMongoRegistry(
    __mongo_database["booking_facilities"]
)
