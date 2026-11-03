
from langchain_core.documents import Document

from app.knowledge_base.chunker import split_documents


def test_split_documents():
    content = " ".join(
        [f"This is sentence number {i}." for i in range(100)]
    )

    documents = [
        Document(
            page_content=content,
            metadata={"source": "return_policy.md"}
        )
    ]

    chunks = split_documents(
        documents,
        chunk_size=200,
        chunk_overlap=40
    )

    assert len(chunks) > 1

    for chunk in chunks:
        assert len(chunk.page_content) <= 200
        assert chunk.metadata["source"] == "return_policy.md"


def test_empty_documents():
    chunks = split_documents([])

    assert chunks == []


def test_invalid_chunk_configuration():
    documents = [
        Document(page_content="Some content", metadata={})
    ]

    try:
        split_documents(
            documents,
            chunk_size=100,
            chunk_overlap=100
        )
        assert False, "Expected ValueError"
    except ValueError:
        pass
