from pathlib import Path

from app.rag.pdf_loader import (
    load_pdf,
    split_text,
)

from app.rag.embeddings import (
    embed_document,
)

from app.rag.vector_store import (
    add_documents,
)


DOCUMENTS_DIR = Path(
    "rag/documents"
)


def index_pdf(pdf_path: str):
    """
    Indexe un PDF complet dans ChromaDB.
    """

    pdf = Path(pdf_path)

    print(
        f"Indexation du document : {pdf.name}"
    )

    text = load_pdf(str(pdf))

    chunks = split_text(text)

    print(
        f"Nombre de chunks : {len(chunks)}"
    )

    embeddings = []

    metadatas = []

    ids = []

    for index, chunk in enumerate(chunks):

        print(
            f"Embedding {index + 1}/{len(chunks)}"
        )

        embedding = embed_document(
            chunk
        )

        embeddings.append(
            embedding
        )

        metadatas.append(
            {
                "source": pdf.name,
                "chunk": index,
            }
        )

        ids.append(
            f"{pdf.stem}-{index}"
        )

    add_documents(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )

    print(
        f"Document indexé : {pdf.name}"
    )


def index_all_pdfs():
    """
    Indexe tous les PDF du dossier.
    """

    pdf_files = list(
        DOCUMENTS_DIR.glob("*.pdf")
    )

    if not pdf_files:
        print(
            "Aucun PDF trouvé dans "
            f"{DOCUMENTS_DIR}"
        )

        return

    for pdf in pdf_files:
        index_pdf(str(pdf))
