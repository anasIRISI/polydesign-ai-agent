
from pathlib import Path

import chromadb


VECTORSTORE_PATH = Path("rag/vectorstore")

VECTORSTORE_PATH.mkdir(
    parents=True,
    exist_ok=True
)


client = chromadb.PersistentClient(
    path=str(VECTORSTORE_PATH)
)


collection = client.get_or_create_collection(
    name="polydesign_documents"
)


def add_documents(
    documents,
    embeddings,
    metadatas,
    ids,
):
    """
    Ajoute des chunks dans ChromaDB.
    """

    if not documents:
        return

    collection.add(
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas,
        ids=ids,
    )


def search_documents(
    query_embedding,
    top_k: int = 5,
):
    """
    Recherche les chunks les plus proches.
    """

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
    )

    return results

