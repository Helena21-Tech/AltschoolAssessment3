from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "StudentAssignmentSystem"
    API_V1_PREFIX: str = "/api/v1"
    ENVIRONMENT: str = ""

    # SECRET_KEY: str
    # ALGORITHM: str = 'HS256'
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # DB
    # default is your local dev DB; can be overridden with env DATABASE_URL
    DATABASE_URL_ASYNC: str = ""
    DATABASE_URL: str = ""
    TEST_DATABASE_URL_ASYNC: str = ""

    # Pydantic v2 settings config
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # ignore unexpected env vars like DEBUG/whatever
    )


settings = Settings()