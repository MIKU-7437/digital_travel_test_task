import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pydantic import PostgresDsn

load_dotenv()


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = '/api'


class DatabaseConfig(BaseModel):
    user: str = os.getenv('POSTGRES_USER', 'postgres')
    password: str = os.getenv("POSTGRES_PASSWORD", '1234')
    host: str = os.getenv('POSTGRES_HOST', 'localhost')
    port: int = os.getenv('POSTGRES_PORT', '5432')
    database: str = os.getenv('POSTGRES_DB', 'authService')

    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        # env_nested_delimiter="_",
        # env_prefix="APP_CONFIG__",

    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()

settings = Settings()
