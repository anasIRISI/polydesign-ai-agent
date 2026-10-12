
import os
from dotenv import load_dotenv
from google import genai

# Charger les variables du fichier .env
load_dotenv()

# Vérifier que la clé existe
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY est absente du fichier .env"
    )

# Créer le client Gemini
client = genai.Client(api_key=api_key)


def generate_response(prompt: str) -> str:
    """
    Envoie un prompt à Gemini et retourne la réponse texte.
    """
    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt
    )

    return response.text
