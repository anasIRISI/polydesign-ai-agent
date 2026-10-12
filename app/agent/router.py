import json

from app.llm.gemini import client
from app.agent.domain_tools import DOMAIN_TOOLS


DOMAIN_DESCRIPTIONS = {
    "cartons": (
        "Questions concernant les cartons, références de cartons, "
        "machines, cellules ou shifts liés aux cartons."
    ),

    "efficience": (
        "Questions concernant l'efficience des cellules, "
        "opérateurs ou shifts."
    ),

    "affectations": (
        "Questions concernant les affectations des employés, "
        "cellules, blocs et emplacements."
    ),

    "blocages": (
        "Questions concernant les blocages de production, "
        "leur durée, leurs causes, descriptions, cellules, "
        "shifts et périodes."
    ),
    "cellules": (
    "Questions concernant les cellules de production, "
    "leur identifiant, leur libellé, leur zone, leur effectif "
    "ou leur ressource principale."
),

"conformes": (
    "Questions concernant les pièces conformes, "
    "les cartons conformes, les références conformes, "
    "les scans conformes et les quantités conformes par date."
),

"carton": (
    "Questions concernant la production dans les cartons, "
    "les quantités produites, les cartons complets, "
    "les états des cartons, la production par jour ou par date, "
    "et les quantités par référence et cellule."
),

"pieces_annulee": (
    "Questions concernant les pièces annulées, "
    "les pièces annulées par code-barres, les annulations par carton, "
    "les annulations par référence, les annulations par date "
    "et les résumés d'annulations par cellule."
),

"pointage": (
    "Questions concernant le pointage des employés, "
    "le pointage d'un employé par matricule, "
    "le pointage d'un employé à une date donnée, "
    "le nombre d'employés ayant pointé dans une cellule "
    "ou le nombre d'employés ayant pointé dans chaque cellule."
),

"rework": (
    "Questions concernant les reworks, "
    "les reworks associés à un code-barres, "
    "les reworks par référence, par défaut, "
    "par opérateur ou par date."
),

"scrap": (
    "Questions concernant les scraps, "
    "les scraps associés à un code-barres, "
    "les scraps par référence, par cellule, par défaut, "
    "par opérateur, par date, ou par référence et défaut."
),

"rag": (
    "Questions concernant les documents, procédures, "
    "instructions, guides, manuels et informations "
    "contenues dans les documents de l'entreprise."
),
}


def detect_domains(question: str,  conversation_context: str = "") -> list[str]:

    domains_text = "\n".join(
        f"- {name}: {description}"
        for name, description in DOMAIN_DESCRIPTIONS.items()
    )

    prompt = f"""
Tu es un routeur pour un assistant industriel.

Ton rôle est de déterminer quels domaines sont nécessaires
pour répondre à la question de l'utilisateur.

IMPORTANT :
La question actuelle peut être une suite d'une conversation précédente.

Tu dois donc utiliser le contexte précédent pour comprendre
les références comme :
- "cellule 17"
- "et pour le 18 ?"
- "demain"
- "et le matricule 5592 ?"
- "la même chose"
- "celle avec la plus faible"

Si la question actuelle est ambiguë seule mais devient claire
avec le contexte, utilise le contexte.

Domaines disponibles :

{domains_text}

Une question peut nécessiter plusieurs domaines.

Exemples :

Question :
"Combien de cartons avons-nous par cellule ?"

Réponse :
{{"domains": ["cartons"]}}

Question :
"Quelle cellule a la meilleure efficience le 17/04/2023 ?"

Réponse :
{{"domains": ["efficience"]}}

Question :
"Quelle est l'efficience de la cellule 19 et combien de cartons
a-t-elle produits ?"

Réponse :
{{"domains": ["efficience", "cartons"]}}

Question :
"Qui travaille dans la cellule 19 ?"

Réponse :
{{"domains": ["affectations"]}}

Question :
"Quels sont les blocages de la cellule 16 ?"

Réponse :
{{"domains": ["blocages"]}}

Question :
"Quelles sont les causes principales des blocages ?"

Réponse :
{{"domains": ["blocages"]}}

Question :
"Quel est l'effectif de la cellule 19 ?"

Réponse :
{{"domains": ["cellules"]}}

Question :
"Quelles cellules appartiennent à la zone 2 ?"

Réponse :
{{"domains": ["cellules"]}}

Question :
"Donne-moi les informations de la cellule 19."

Réponse :
{{"domains": ["cellules"]}}

Question :
"Combien de pièces conformes avons-nous dans le carton 280519102 ?"

Réponse :
{{"domains": ["conformes"]}}

Question :
"Combien de pièces conformes avons-nous pour la référence 9CS178221TSZ ?"

Réponse :
{{"domains": ["conformes"]}}

Question :
"Combien de pièces conformes avons-nous eu le 17/04/2023 ?"

Réponse :
{{"domains": ["conformes"]}}

Question :
"Quelles références ont le plus de pièces conformes ?"

Réponse :
{{"domains": ["conformes"]}}

Question :
"Quelle quantité totale a été produite dans la cellule 19 ?"

Réponse :
{{"domains": ["carton"]}}

Question :
"Quelle est la production par jour ?"

Réponse :
{{"domains": ["carton"]}}

Question :
"Combien de cartons sont complets ?"

Réponse :
{{"domains": ["carton"]}}

Question :
"Combien de cartons avons-nous sur la machine 192.168.100.104 ?"

Réponse :
{{"domains": ["cartons"]}}

Question :
"Quelle pièce a été annulée avec le code-barres 123456 ?"

Réponse :
{{"domains": ["pieces_annulee"]}}

Question :
"Quelles pièces ont été annulées dans le carton 280519102 ?"

Réponse :
{{"domains": ["pieces_annulee"]}}

Question :
"Combien d'annulations avons-nous par référence ?"

Réponse :
{{"domains": ["pieces_annulee"]}}

Question :
"Combien de pièces ont été annulées le 17/04/2023 ?"

Réponse :
{{"domains": ["pieces_annulee"]}}

Question :
"Donne-moi le résumé des annulations de la cellule 19."

Réponse :
{{"domains": ["pieces_annulee"]}}

Question :

"Donne-moi le pointage de l'employé 5592."

Réponse :

{{"domains": ["pointage"]}}

Question :

"Quel était le pointage de l'employé 5592 le 17/04/2023 ?"

Réponse :

{{"domains": ["pointage"]}}

Question :

"Combien d'employés ont pointé dans la cellule 19 le 17/04/2023 ?"

Réponse :

{{"domains": ["pointage"]}}

Question :

"Combien d'employés ont pointé dans chaque cellule le 17/04/2023 ?"

Réponse :

{{"domains": ["pointage"]}}

Question :

"Quels reworks sont associés au code-barres 123456 ?"

Réponse :

{{"domains": ["rework"]}}

Question :

"Donne-moi les reworks de la référence 9CS178221TSZ."

Réponse :

{{"domains": ["rework"]}}

Question :

"Combien avons-nous de reworks par référence ?"

Réponse :

{{"domains": ["rework"]}}

Question :

"Quels sont les défauts qui génèrent le plus de reworks ?"

Réponse :

{{"domains": ["rework"]}}

Question :

"Donne-moi les reworks de l'opérateur 5592."

Réponse :

{{"domains": ["rework"]}}

Question :

"Combien de reworks avons-nous le 17/04/2023 ?"

Réponse :

{{"domains": ["rework"]}}

Question :

"Quel scrap est associé au code-barres 123456 ?"

Réponse :

{{"domains": ["scrap"]}}

Question :

"Quels scraps sont associés à la référence 9CS178221TSZ ?"

Réponse :

{{"domains": ["scrap"]}}

Question :

"Quels sont les scraps de la cellule 19 ?"

Réponse :

{{"domains": ["scrap"]}}

Question :

"Quels sont les défauts qui génèrent le plus de scraps ?"

Réponse :

{{"domains": ["scrap"]}}

Question :

"Combien de scraps avons-nous par opérateur ?"

Réponse :

{{"domains": ["scrap"]}}

Question :

"Combien de scraps a généré l'opérateur 5592 ?"

Réponse :

{{"domains": ["scrap"]}}

Question :

"Combien de scraps avons-nous le 17/04/2023 ?"

Réponse :

{{"domains": ["scrap"]}}

Question :

"Donne-moi le nombre de scraps par référence et par défaut."

Réponse :

{{"domains": ["scrap"]}}

Contexte de conversation précédent :
{conversation_context}

Question utilisateur :
{question}

Réponds uniquement avec un objet JSON valide.

Format obligatoire :

{{
    "domains": ["nom_du_domaine"]
}}

Les domaines autorisés sont uniquement :

{list(DOMAIN_TOOLS.keys())}
"""

    # ========================================================
    # APPEL GEMINI
    # ========================================================

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
        },
    )

    # ========================================================
    # DEBUG
    # ========================================================

    text = response.text.strip()

    print("\n==============================")
    print("REPONSE ROUTER")
    print("==============================")
    print(text)

    # ========================================================
    # VERIFICATION REPONSE VIDE
    # ========================================================

    if not text:
        raise ValueError(
            "Le Router Gemini a retourné une réponse vide."
        )

    # ========================================================
    # PARSE JSON
    # ========================================================

    try:
        data = json.loads(text)

    except json.JSONDecodeError as e:

        raise ValueError(
            f"Le Router n'a pas retourné un JSON valide.\n"
            f"Réponse reçue : {text}"
        ) from e

    # ========================================================
    # RECUPERER LES DOMAINES
    # ========================================================

    domains = data.get("domains", [])

    # Vérification
    if not isinstance(domains, list):
        raise ValueError(
            "Le champ 'domains' doit être une liste."
        )

    # ========================================================
    # SECURITE
    # ========================================================

    domains = [
        domain
        for domain in domains
        if domain in DOMAIN_TOOLS
    ]

    return domains