from google import genai
from .config import GEMINI_key
from google.genai import types
from pydantic import BaseModel, Field
from typing import Literal 




class TourismAnalysis(BaseModel):
    summary: str = Field(description="Résumé du texte analysé.")
    ton: Literal["positif", "negatif", "neutre"] = Field(
        description="Le ton général du texte, doit être l'une des trois valeurs.")


def gemini_result(prompt):
    client = genai.Client(api_key=GEMINI_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
                Analyse le texte suivant :
                \"\"\"{prompt}\"\"\"

                1. Fais un résumé clair et concis du texte.
                2. Détermine le ton général du texte. Choisis UNIQUEMENT parmi :
                - "positif"
                - "negatif"
                - "neutre"

                Retourne la réponse UNIQUEMENT en JSON respectant strictement ce schéma : """,

        config={"response_mime_type": "application/json",
                "response_schema": TourismAnalysis,
               }
    )
    
    result= TourismAnalysis.model_validate_json(response.text)
    print(result)

    return result
if __name__ == "__main__":
    prompt = "Agadir attire chaque année de nombreux visiteurs grâce à sa plage ensoleillée,sa corniche moderne, et ses infrastructures touristiques en développement.Cependant, la ville doit faire face à la saisonnalité du tourism et à la nécessité de diversifier son offre.Retourne le résultat UNIQUEMENT en JSON."

    gemini_result(prompt)

