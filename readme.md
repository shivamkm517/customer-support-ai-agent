# ShopEase — AI Customer Support Agent

An AI-powered customer support system for an e-commerce platform, built using Python, FastAPI, LangChain, Cohere embeddings, Qdrant, and LangGraph (planned).

The project aims to automate customer support operations such as order-status inquiries, customer information retrieval, policy-based question answering, support-ticket creation, and human escalation.

> **Project status:** Under active development. The foundation, database tools, document processing, Cohere embeddings, and Qdrant vector storage have been implemented. LangGraph agent orchestration and complete RAG integration are upcoming milestones.

---

## 1. Project Objectives

The main objectives of ShopEase are:

- Answer customer questions using company knowledge-base documents.
- Retrieve order information and customer details.
- Create support tickets for customer issues.
- Escalate unresolved issues to human support.
- Maintain conversation context across multiple messages.
- Use an AI agent to decide which tool or action is required.

## 2. Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python |
| Backend framework | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Data validation | Pydantic |
| AI framework | LangChain |
| Agent orchestration | LangGraph (planned) |
| Embedding model | Cohere `embed-v4.0` |
| Embedding dimension | 1024 |
| Vector database | Qdrant Local |
| Document processing | PyPDF |
| Text chunking | LangChain Text Splitters |
| Testing | Pytest |

## 3. Current Architecture

```text
                 ShopEase AI Support
                         |
                  FastAPI Application
                         |
              -----------------------
              |                     |
         Database Layer        Support Tools
              |                     |
          SQLite DB          -------------------
                             |        |        |
                           Orders  Customer  Tickets
                                      |
                                  Escalation

              Knowledge Base / RAG
                         |
                 Document Loader
                         |
                   Text Chunker
                         |
                 Cohere Embeddings
                    embed-v4.0
                         |
                   Qdrant Local
                         |
                  Semantic Search
```

LangGraph will later coordinate the support tools, retrieval workflow, and response generation.

## 4. Project Structure

```text
shopsee/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── models.py
│   │   ├── crud.py
│   │   ├── init_db.py
│   │   └── seed.py
│   │
│   ├── tools/
│   │   ├── customer_tool.py
│   │   ├── order_tool.py
│   │   ├── ticket_tool.py
│   │   └── escalation_tool.py
│   │
│   └── knowledge_base/
│       ├── loader.py
│       ├── chunker.py
│       ├── embeddings.py
│       ├── vector_store.py
│       └── ingestion.py
│
├── data/
│   └── knowledge_base/
│       ├── refund_policy.md
│       ├── return_policy.md
│       └── shipping_policy.md
│
├── test/
│   ├── test_config.py
│   ├── test_crud.py
│   ├── test_customer_tool.py
│   ├── test_order_tool.py
│   ├── test_ticket_tool.py
│   ├── test_embeddings.py
│   ├── test_loader.py
│   ├── test_chunker.py
│   └── test_vector_store.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── readme.md
```

## 5. Implemented Features

### A. Backend Foundation
- FastAPI application initialization.
- Centralized application configuration.
- Environment-variable management using Pydantic Settings.
- Health-check endpoint.

### B. Database Layer
- SQLAlchemy database connection.
- SQLite database initialization.
- Database models for:
  - Customers
  - Orders
  - Conversations
  - Messages
  - Support tickets
- CRUD operations for customer, order, and ticket data.
- Database seeding script.

### C. Customer Support Tools

The project currently includes the following support tools:

| Tool | Responsibility |
|---|---|
| `get_customer_details` | Retrieve customer information |
| `get_order_status` | Retrieve order status with customer ownership validation |
| `create_support_ticket` | Create a support ticket |
| `escalate_to_human` | Create a high-priority human-escalation ticket |

These tools are implemented as LangChain tools.

### D. Knowledge Base Processing

Supported document formats:
- PDF
- TXT
- Markdown

Implemented functionality:
- Load documents from the knowledge-base directory.
- Extract PDF text page by page.
- Preserve source metadata.
- Split documents into smaller chunks.
- Configure chunk size and overlap.

### E. Embedding Generation

Using Cohere's `embed-v4.0` model:

- Generate document embeddings.
- Generate query embeddings.
- Use `search_document` for document embeddings.
- Use `search_query` for query embeddings.
- Generate 1024-dimensional vectors.

### F. Vector Storage and Retrieval

Using Qdrant Local:

- Create a persistent local vector collection.
- Store document vectors.
- Store document content and metadata as payload.
- Perform semantic similarity searches using cosine distance.
- Retrieve relevant document chunks for a query.

### G. Testing

Pytest is used to validate individual components.

Current test coverage includes:
- Application configuration.
- Database CRUD operations.
- Customer, order, and ticket tools.
- LangChain tool integration.
- Document loading.
- Text chunking.
- Cohere embedding functions.
- Qdrant vector storage and semantic search.

## 6. Installation and Setup

### Prerequisites

- Python 3.10+
- Git
- Cohere API key

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd shopsee
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure environment variables

Create a `.env` file in the project root.

```env
APP_NAME=ShopEase AI Support
ENVIRONMENT=development
DEBUG=True

DATABASE_URL=sqlite:///./shop.db

COHERE_API_KEY=your_cohere_api_key
COHERE_EMBEDDING_MODEL=embed-v4.0
COHERE_EMBEDDING_DIMENSION=1024

QDRANT_PATH=./qdrant_data
QDRANT_COLLECTION_NAME=shopease_knowledge_base
```

Never commit your actual `.env` file or API keys to GitHub.

### Step 5: Initialize the database

```bash
python -m app.database.init_db
```

### Step 6: Run the FastAPI application

```bash
uvicorn app.main:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## 7. Knowledge Base Ingestion

The ingestion module connects document loading, chunking, embedding generation, and vector storage.

Run:

```bash
python -c "from app.knowledge_base.ingestion import ingest_knowledge_base; print(ingest_knowledge_base())"
```

The pipeline processes documents from:

```text
data/knowledge_base/
```

The generated vectors are persisted locally in:

```text
qdrant_data/
```

Note: The current implementation appends vectors. Duplicate prevention and document-update handling are future improvements.

## 8. Running Tests

Run the complete test suite:

```bash
python -m pytest test/ -v
```

Run an individual test:

```bash
python -m pytest test/test_vector_store.py -v
```

## 9. Development Roadmap

The project is being developed incrementally.

- [x] FastAPI application foundation
- [x] Environment configuration
- [x] Database models and CRUD operations
- [x] Customer support tools
- [x] Document loading
- [x] Document chunking
- [x] Cohere embedding integration
- [x] Qdrant local vector storage
- [x] Semantic search
- [x] Initial component tests
- [ ] Complete and validate knowledge-base ingestion
- [ ] Implement `search_faq` tool
- [ ] Integrate RAG with LangGraph
- [ ] Implement intent classification and tool routing
- [ ] Implement response generation with source grounding
- [ ] Implement conversation memory
- [ ] Integrate all functionality with FastAPI endpoints
- [ ] Implement human-in-the-loop workflow
- [ ] Add comprehensive end-to-end tests
- [ ] Add Docker deployment

## 10. Engineering Principles

The project follows these development principles:

- Modular and maintainable architecture.
- Separation of database, business logic, and AI components.
- Reusable support tools.
- Environment-based configuration.
- Test-driven validation of individual components.
- Grounded responses using company knowledge-base data.
- Incremental implementation and meaningful Git commits.

---

**ShopEase AI Customer Support Agent**

*An ongoing learning and engineering project focused on building practical AI-powered customer support systems using RAG, vector databases, and agentic workflows.*
