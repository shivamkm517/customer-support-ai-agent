
from langchain_core.documents import Document

from app.knowledge_base.vector_store import (
    create_collection,
    store_documents,
    search_documents,
)


def test_qdrant_vector_store():
    documents = [
        Document(
            page_content="ShopEase allows product returns within 7 days.",
            metadata={"source": "return_policy.md"},
        ),
        Document(
            page_content="Refunds are processed within 5 to 7 business days.",
            metadata={"source": "refund_policy.md"},
        ),
        Document(
            page_content="Orders are usually delivered within 3 to 5 days.",
            metadata={"source": "shipping_policy.md"},
        ),
    ]

    collection = create_collection()
    assert collection == "shopease_knowledge_base"

    count = store_documents(documents)
    assert count == 3

    results = search_documents(
        "How many days do I have to return a product?",
        limit=2,
    )

    assert len(results) > 0
    assert "return" in results[0]["content"].lower()
    assert results[0]["score"] is not None
