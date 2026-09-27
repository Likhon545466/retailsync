import os
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    APP_NAME: str = "RetailSync - Enterprise Super Shop WMS"
    APP_VERSION: str = "1.0.0-RELEASE"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Database: Supports SQLite (zero-config local) or PostgreSQL (production/docker)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./retailsync.db")
    
    # JWT Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "retailsync_diu_capstone_super_secret_jwt_key_2026")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 12 # 12 hours for convenient defense demo
    
    # Academic Attribution
    INSTITUTION: str = "Daffodil International University (DIU)"
    DEPARTMENT: str = "Department of Software Engineering"
    COURSE: str = "SE-231: Capstone Project 2"
    TEAM_MEMBERS: list[dict] = [
        {"name": "Raisul Islam Likhon", "id": "251-35-508", "role": "Project Lead"},
        {"name": "Shottobroto Dey", "id": "251-35-017", "role": "Core Developer"},
        {"name": "Golam Husnain Papon", "id": "251-35-529", "role": "Core Developer"}
    ]
    BATCH: str = "44th Batch"
    SECTION: str = "SWE-44D"

    class Config:
        env_file = ".env"
        extra = "allow"

settings = Settings()
