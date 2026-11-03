from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_NAME: str = "ShopEase AI Support"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    DATABASE_URL: str = "sqlite:///./shop.db"

    LLM_PROVIDER: str = "openai"
    LLM_MODEL: str = "gpt-4o-mini"

    COHERE_API_KEY: str | None = None
    COHERE_EMBEDDING_MODEL: str = "embed-v4.0"
    COHERE_EMBEDDING_DIMENSION: int = 1024

    QDRANT_PATH: str = "./qdrant_data"
    QDRANT_COLLECTION_NAME: str = "shopease_knowledge_base"
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()