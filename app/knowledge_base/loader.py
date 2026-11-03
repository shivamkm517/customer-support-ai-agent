
from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document


SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".md"}


def load_document(file_path: str) -> list[Document]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {extension}")

    documents = []

    if extension == ".pdf":
        reader = PdfReader(str(path))

        for page_number, page in enumerate(reader.pages, start=1):
            content = page.extract_text() or ""

            if content.strip():
                documents.append(
                    Document(
                        page_content=content,
                        metadata={
                            "source": str(path),
                            "page": page_number
                        }
                    )
                )

    else:
        content = path.read_text(encoding="utf-8")

        if content.strip():
            documents.append(
                Document(
                    page_content=content,
                    metadata={
                        "source": str(path)
                    }
                )
            )

    return documents


def load_documents(directory: str) -> list[Document]:
    directory_path = Path(directory)

    if not directory_path.is_dir():
        raise NotADirectoryError(
            f"Directory not found: {directory}"
        )

    documents = []

    for path in sorted(directory_path.rglob("*")):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            documents.extend(load_document(str(path)))

    return documents
