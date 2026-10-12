
from app.rag.embeddings import (
    embed_query,
)

from app.rag.vector_store import (
    search_documents,
)


def rechercher_documents(
    question: str,
    top_k: int = 5,
):
    """
    Recherche les passages pertinents
    dans les documents indexés.
    """

    query_embedding = embed_query(
        question
    )

    results = search_documents(
        query_embedding=query_embedding,
        top_k=top_k,
    )

    documents = results.get(
        "documents",
        [[]]
    )[0]

    metadatas = results.get(
        "metadatas",
        [[]]
    )[0]

    output = []

    for document, metadata in zip(
        documents,
        metadatas
    ):

        output.append(
            {
                "source": metadata.get(
                    "source"
                ),
                "chunk": metadata.get(
                    "chunk"
                ),
                "content": document,
            }
        )

    return output
