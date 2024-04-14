from pydantic_settings import BaseSettings, SettingsConfigDict


class MongoSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="mongo_")
    username: str
    password: str
    host: str
    port: int
    database_name: str
    url: str = f"mongodb+srv://{username}:{password}@{host}:{port}/{database_name}"


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    mongodb: MongoSettings = MongoSettings()


settings = Settings()
