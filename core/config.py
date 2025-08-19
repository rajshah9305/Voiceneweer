# core/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Manages application settings and secrets using Pydantic.
    Loads variables from a .env file.
    """
    # ELEVENLABS_API_KEY: str # Commented out as per user request

    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8") # Commented out as per user request

settings = Settings()


