from google import genai
from .config import GEMINI_key
from .hf_services import hagginface_classifier
from google.genai import types
from pydantic import BaseModel, Field
from typing import Literal 




class ResponsAnalysis(BaseModel):
    summary: str = Field(description="Résumé du texte analysé.")
    ton: Literal["positif", "negatif", "neutre"] = Field(description="Le ton général du texte, doit être l'une des trois valeurs.")
    score: float 
    category: str


def gemini_result(text, category, score):
    client = genai.Client(api_key=GEMINI_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
                Analyse le texte suivant :
                \"\"\"{text}\"\"\"
                et dont la catégorie : {category} et le score : {score}

                1. Fais un résumé clair et concis du texte.
                2. Détermine le ton général du texte. Choisis UNIQUEMENT parmi :
                - "positif"
                - "negatif"
                - "neutre"

                Retourne la réponse UNIQUEMENT en JSON respectant strictement ce schéma  indiquant la category et le score: """,

        config={"response_mime_type": "application/json",
                "response_schema": ResponsAnalysis,
               }
    )
    
    result= response.text
    print(result)

    return result

def hybrd_analyzer(text):
    category, score = hagginface_classifier(text)

    return gemini_result(text, category, score)
    
