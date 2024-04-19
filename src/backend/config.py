import os

from pydantic_settings import BaseSettings


class MongoSettings(BaseSettings):
    username: str = os.getenv("MONGO_USERNAME")
    password: str = os.getenv("MONGO_PASSWORD")
    host: str = os.getenv("MONGO_HOST")
    port: int = int(os.getenv("MONGO_PORT"))
    database_name: str = os.getenv("MONGO_DATABASE_NAME")
    url: str = f"mongodb+srv://{username}:{password}@{host}:{port}/{database_name}"


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    mongodb: MongoSettings = MongoSettings()


settings = Settings()
