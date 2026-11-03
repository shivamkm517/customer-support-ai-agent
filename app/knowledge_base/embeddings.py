
import cohere

from app.core.config import settings


def get_cohere_client():
    if not settings.COHERE_API_KEY:
        raise ValueError("COHERE_API_KEY is not configured")

    return cohere.ClientV2(
        api_key=settings.COHERE_API_KEY
    )


def embed_documents(texts: list[str]) -> list[list[float]]:
    if not texts:
        return []

    client = get_cohere_client()

    response = client.embed(
        texts=texts,
        model=settings.COHERE_EMBEDDING_MODEL,
        input_type="search_document",
        output_dimension=settings.COHERE_EMBEDDING_DIMENSION,
        embedding_types=["float"]
    )

    return response.embeddings.float


def embed_query(query: str) -> list[float]:
    client = get_cohere_client()

    response = client.embed(
        texts=[query],
        model=settings.COHERE_EMBEDDING_MODEL,
        input_type="search_query",
        output_dimension=settings.COHERE_EMBEDDING_DIMENSION,
        embedding_types=["float"]
    )

    return response.embeddings.float[0]
