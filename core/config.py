# core/config.py
from decouple import config, Csv

class Settings:
    PORT: int = config("PORT", default=8000, cast=int)
    MINI_API_KEY: str = config("MINI_API_KEY")
    ALLOWED_DOMAINS: list[str] = config("ALLOWED_DOMAINS", cast=Csv())

settings = Settings()