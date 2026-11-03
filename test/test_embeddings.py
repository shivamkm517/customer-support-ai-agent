
from unittest.mock import patch, MagicMock

import pytest

from app.knowledge_base.embeddings import (
    embed_documents,
    embed_query,
    get_cohere_client
)


@patch("app.knowledge_base.embeddings.get_cohere_client")
def test_embed_documents(mock_client):
    mock_response = MagicMock()

    mock_response.embeddings.float = [
        [0.1] * 1024,
        [0.2] * 1024
    ]

    mock_client.return_value.embed.return_value = mock_response

    result = embed_documents([
        "Return policy",
        "Shipping policy"
    ])

    assert len(result) == 2
    assert len(result[0]) == 1024


@patch("app.knowledge_base.embeddings.get_cohere_client")
def test_embed_query(mock_client):
    mock_response = MagicMock()
    mock_response.embeddings.float = [[0.1] * 1024]

    mock_client.return_value.embed.return_value = mock_response

    result = embed_query("What is the refund policy?")

    assert len(result) == 1024


def test_empty_documents():
    assert embed_documents([]) == []


def test_missing_api_key(monkeypatch):
    from app.knowledge_base import embeddings

    monkeypatch.setattr(
        embeddings.settings,
        "COHERE_API_KEY",
        None
    )

    with pytest.raises(ValueError):
        get_cohere_client()
