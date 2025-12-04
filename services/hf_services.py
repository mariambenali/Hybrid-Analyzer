import os
import requests



def prompt(text:str):

    API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
    headers = {
        "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    }
    payload= {
        "inputs": text,
        "parameters": {"candidate_labels": ["tourisme", "climat", "hôtels", "transport", "culture"]},
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    data = response.json()   # C'est UNE LISTE de dictionnaires

    # Trouver l’élément avec le score max
    best_item = max(data, key=lambda x: x["score"])

    return best_item["label"]


myprompt = prompt("Agadir est une destination très visitée...")

print(myprompt)