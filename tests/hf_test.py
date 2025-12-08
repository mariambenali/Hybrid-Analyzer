import pytest
from unittest.mock import patch
from services.hf_services import hagginface_classifier
from services.gemini_services import gemini_result


@patch("services.hf_services.requests.post")
def test_hugginface(mock_post):

    # définir le mock avant l’appel
    mock_post.return_value.json.return_value = [
        {"label": "tourism", "score": 0.92}
    ]

    # appeler la fonction
    label, score = hagginface_classifier("Agadir est magnifique")

    # sssertions
    assert isinstance(label, str)
    assert isinstance(score, float)
    assert label == "tourism"
    assert score == 0.92


'''class ResponsAnalysis(BaseModel):
    summary: str = Field(description="Résumé du texte analysé.")
    ton: Literal["positif", "negatif", "neutre"] = Field(description="Le ton général du texte, doit être l'une des trois valeurs.")
    score: float 
    category: str
'''

@patch("services.gemini_services.genai.client.Models.generate_content")
def test_gemini(mock_post):

    #définir le mock
    mock_post.return_value.text = """{
            "summary": "Résumé test",
            "ton": "negatif",
            "score" : 0.92,
            "category": "tourism"
        }"""
    
    summary = "Résumé test"
    ton =  "negatif"
    

    #appler la fonction

    result = gemini_result("texte test", "tourism", 0.95)
    print(result)

    #assertion

    assert summary in result 
    assert ton in result