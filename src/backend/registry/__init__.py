from .async_mongo_registry import (  # noqa: F401
    AsyncMongoRegistryFactory,  # noqa: F401
    AsyncMongoRegistry,  # noqa: F401
    AsyncRegistry,  # noqa: F401
)
from .mongo_helper import mongo_helper, AsyncDBHelper  # noqa: F401

mongo_registry_factory = AsyncMongoRegistryFactory(mongo_helper.get_database())

UserMongoRegistry = mongo_registry_factory.get_registry("users")
BookingFacilitiesMongoRegistry = mongo_registry_factory.get_registry(
    "booking_facilities"
)
