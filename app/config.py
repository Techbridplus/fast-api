from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    database_url: str | None = Field(default=None, alias="DATABASE_URL")  # optional full URL

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()