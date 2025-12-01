from google import genai
from config import GEMINI_key
from google.genai import types
from pydantic import BaseModel, Field
from typing import List, Optional




class TourismFactor(BaseModel):
    factor: str = Field(description="Facteur touristique mentionné dans le texte concernant Agadir.")
    effect: Optional[str] = Field(description="Impact de ce facteur sur le tourisme local.")


class TourismAnalysis(BaseModel):
    summary: str = Field(description="Résumé du texte analysé.")
    main_theme: str = Field(description="Thème principal lié à la destination d'Agadir.")
    factors: List[TourismFactor] = Field(description="Facteurs influençant le tourisme à Agadir.")
    consequences: List[str] = Field(description="Effets économiques, sociaux ou environnementaux.")
    stakeholders: List[str] = Field(description="Acteurs concernés (touristes, hôtels, agences, autorités...).")
    conclusion: Optional[str] = Field(description="Conclusion globale sur la situation touristique.", default=None)


client = genai.Client(api_key=GEMINI_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="""
Analyse touristiquement ce texte :

Agadir attire chaque année de nombreux visiteurs grâce à sa plage ensoleillée,
sa corniche moderne, et ses infrastructures touristiques en développement.
Cependant, la ville doit faire face à la saisonnalité du tourisme
et à la nécessité de diversifier son offre.

Retourne le résultat UNIQUEMENT en JSON.
""",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
)

print(response.text)