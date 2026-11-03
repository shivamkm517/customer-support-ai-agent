
from uuid import uuid4

from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    PointStruct,
    VectorParams,
)

from app.core.config import settings
from app.knowledge_base.embeddings import (
    embed_documents,
    embed_query,
)

_client = None


def get_qdrant_client():
    global _client

    if _client is None:
        _client = QdrantClient(path=settings.QDRANT_PATH)

    return _client


def create_collection():
    client = get_qdrant_client()

    collection_name = settings.QDRANT_COLLECTION_NAME

    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=settings.COHERE_EMBEDDING_DIMENSION,
                distance=Distance.COSINE,
            ),
        )

    return collection_name


def store_documents(documents):
    if not documents:
        return 0

    collection_name = create_collection()
    client = get_qdrant_client()

    stored_count = 0

    # Cohere supports up to 96 texts per embedding request.
    for start in range(0, len(documents), 96):
        batch = documents[start:start + 96]

        texts = [doc.page_content for doc in batch]
        vectors = embed_documents(texts)

        points = []

        for doc, vector in zip(batch, vectors):
            payload = {
                "page_content": doc.page_content,
                "metadata": doc.metadata,
            }

            points.append(
                PointStruct(
                    id=str(uuid4()),
                    vector=vector,
                    payload=payload,
                )
            )

        client.upsert(
            collection_name=collection_name,
            points=points,
        )

        stored_count += len(points)

    return stored_count


def search_documents(query: str, limit: int = 3):
    client = get_qdrant_client()
    collection_name = settings.QDRANT_COLLECTION_NAME

    if not client.collection_exists(collection_name):
        return []

    query_vector = embed_query(query)

    results = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=limit,
        with_payload=True,
    )

    return [
        {
            "content": point.payload["page_content"],
            "metadata": point.payload["metadata"],
            "score": point.score,
        }
        for point in results.points
    ]
