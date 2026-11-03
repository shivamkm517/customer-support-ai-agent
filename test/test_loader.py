
from pathlib import Path

import pytest

from app.knowledge_base.loader import (
    load_document,
    load_documents
)


def test_load_markdown(tmp_path):
    file_path = tmp_path / "policy.md"

    file_path.write_text(
        "# Return Policy\nCustomers can return products within 7 days.",
        encoding="utf-8"
    )

    documents = load_document(str(file_path))

    assert len(documents) == 1
    assert "Return Policy" in documents[0].page_content
    assert documents[0].metadata["source"] == str(file_path)


def test_load_text(tmp_path):
    file_path = tmp_path / "faq.txt"

    file_path.write_text(
        "How long does shipping take? 3-5 business days.",
        encoding="utf-8"
    )

    documents = load_document(str(file_path))

    assert len(documents) == 1
    assert "3-5 business days" in documents[0].page_content


def test_unsupported_file(tmp_path):
    file_path = tmp_path / "data.csv"
    file_path.write_text("some,data")

    with pytest.raises(ValueError):
        load_document(str(file_path))


def test_load_directory(tmp_path):
    (tmp_path / "policy1.md").write_text("Return policy")
    (tmp_path / "policy2.txt").write_text("Shipping policy")

    documents = load_documents(str(tmp_path))

    assert len(documents) == 2
