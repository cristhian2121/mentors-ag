from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    OPENAI_API_KEY: str = ""
    AI_MODEL: str = "gpt-3.5-turbo"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()