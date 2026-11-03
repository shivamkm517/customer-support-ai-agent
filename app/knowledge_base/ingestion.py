
from app.knowledge_base.loader import load_documents
from app.knowledge_base.chunker import split_documents
from app.knowledge_base.vector_store import store_documents


def ingest_knowledge_base(
    directory="data/knowledge_base",
    chunk_size=500,
    chunk_overlap=100,
):
    # 1. Load source documents
    documents = load_documents(directory)

    if not documents:
        return {
            "documents_loaded": 0,
            "chunks_created": 0,
            "chunks_stored": 0,
        }

    # 2. Split documents into chunks
    chunks = split_documents(
        documents,
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )

    # 3. Generate embeddings and store in Qdrant
    stored_count = store_documents(chunks)

    return {
        "documents_loaded": len(documents),
        "chunks_created": len(chunks),
        "chunks_stored": stored_count,
    }
