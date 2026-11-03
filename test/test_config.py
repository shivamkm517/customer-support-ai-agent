
import pytest

from app.core.config import Settings


def test_default_settings():
    settings = Settings(_env_file=None)

    assert settings.APP_NAME == "ShopEase AI Support"
    assert settings.ENVIRONMENT == "development"
    assert settings.DEBUG is True
    assert settings.DATABASE_URL == "sqlite:///./shop.db"


def test_environment_variable_override(monkeypatch):
    monkeypatch.setenv("APP_NAME", "Test Shop")
    monkeypatch.setenv("ENVIRONMENT", "testing")

    settings = Settings(_env_file=None)

    assert settings.APP_NAME == "Test Shop"
    assert settings.ENVIRONMENT == "testing"


def test_boolean_parsing(monkeypatch):
    monkeypatch.setenv("DEBUG", "false")

    settings = Settings(_env_file=None)

    assert settings.DEBUG is False


def test_optional_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    settings = Settings(_env_file=None)

    assert settings.OPENAI_API_KEY is None


def test_api_key_loading(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-api-key")

    settings = Settings(_env_file=None)

    assert settings.OPENAI_API_KEY == "test-api-key"
