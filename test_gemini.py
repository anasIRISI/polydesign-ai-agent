
from app.llm.gemini import generate_response


question = "Explique en une phrase ce qu'est une base de données."

try:
    response = generate_response(question)

    print("====================================")
    print("GEMINI TEST")
    print("====================================")
    print("Question :", question)
    print()
    print("Réponse :")
    print(response)
    print()
    print("✅ Gemini fonctionne correctement.")

except Exception as e:
    print("====================================")
    print("❌ ERREUR GEMINI")
    print("====================================")
    print(type(e).__name__)
    print(str(e))









