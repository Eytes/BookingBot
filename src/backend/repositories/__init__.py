import pymongo

from ..config import settings

client = pymongo.MongoClient(settings.mongodb.url)
booking_bot_db = client[settings.mongodb.database_name]
reservation_collection = booking_bot_db["reservations"]
audience_collection = booking_bot_db["audiences"]
user_collection = booking_bot_db["users"]
