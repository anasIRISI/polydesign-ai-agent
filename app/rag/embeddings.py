import os

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY n'est pas configurée."
    )


client = genai.Client(
    api_key=GEMINI_API_KEY
)


EMBEDDING_MODEL = "gemini-embedding-001"


def embed_document(text: str):
    """
    Génère l'embedding d'un chunk de document.
    """

    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
            output_dimensionality=768,
        ),
    )

    return result.embeddings[0].values


def embed_query(query: str):
    """
    Génère l'embedding d'une question utilisateur.
    """

    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=query,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=768,
        ),
    )

    return result.embeddings[0].values
