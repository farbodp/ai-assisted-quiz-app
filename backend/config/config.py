from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    POSTGRES_DB_URL: str

    class Config:
        env_file = 'backend/.env'

settings = Settings()