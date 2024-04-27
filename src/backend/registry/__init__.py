from .async_mongo_registry import (  # noqa: F401
    AsyncMongoRegistryFactory,  # noqa: F401
    AsyncMongoRegistry,  # noqa: F401
    AsyncRegistry,  # noqa: F401
)
from .mongo_helper import mongo_helper

mongo_registry_factory = AsyncMongoRegistryFactory(mongo_helper.database)

UserMongoRegistry = mongo_registry_factory.get_registry("users")
BookingFacilitiesMongoRegistry = mongo_registry_factory.get_registry(
    "booking_facilities"
)
