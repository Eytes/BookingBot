from .async_mongo_registry import (
    AsyncMongoRegistryFactory,  # noqa: F401
    AsyncMongoRegistry,  # noqa: F401
)
from .mongo_helper import mongo_helper  # noqa: F401

mongo_registry_factory = AsyncMongoRegistryFactory()

UserMongoRegistry = mongo_registry_factory.get_registry("users")
BookingFacilitiesMongoRegistry = mongo_registry_factory.get_registry(
    "booking_facilities"
)
