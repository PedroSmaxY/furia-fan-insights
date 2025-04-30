from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from os import getenv

load_dotenv()


class Settings(BaseSettings):
    DB_URL: str = getenv("DB_URL", "sqlite:///database.db")


settings = Settings()
