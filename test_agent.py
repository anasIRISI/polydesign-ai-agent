
from app.agent.agent import ask_agent


question = " Comment faire un reset de SYSPRO PASSWORD ? ?"
session_id = "test-001"


print("====================================")
print("TEST AI AGENT")
print("====================================")
print()
print("Question :")
print(question)
print("session_id :")
print(session_id)
print()


try:

    response = ask_agent(question,session_id)

    print("====================================")
    print("REPONSE DE L'AGENT")
    print("====================================")
    print(response)
    print()

    print("====================================")
    print("✅ Agent + Gemini + Tool fonctionnent.")
    print("====================================")


except Exception as e:

    print("====================================")
    print("❌ ERREUR AGENT")
    print("====================================")

    print("Type :", type(e).__name__)
    print("Message :", str(e))
