from .async_mongo_registry import AsyncMongoRegistryFactory
from .mongo_helper import mongo_helper

mongo_registry_factory = AsyncMongoRegistryFactory()

UserMongoRegistry = mongo_registry_factory.get_registry("users")
BookingFacilitiesMongoRegistry = mongo_registry_factory.get_registry(
    "booking_facilities"
)
