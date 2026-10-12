
from app.tools.rag_tools import (
    rechercher_documents,
)


if __name__ == "__main__":

    question = input(
        "Question RAG : "
    )

    results = rechercher_documents(
        question,
        top_k=5,
    )

    print()
    print(
        "=============================="
    )
    print(
        "RESULTATS RAG"
    )
    print(
        "=============================="
    )

    if not results:
        print(
            "Aucun résultat."
        )

    for index, result in enumerate(
        results,
        start=1
    ):

        print()
        print(
            f"--- RESULTAT {index} ---"
        )

        print(
            f"Source : {result['source']}"
        )

        print(
            f"Chunk : {result['chunk']}"
        )

        print()

        print(
            result["content"]
        )
