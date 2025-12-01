import os
import requests



def prompt(text:input):

    API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
    headers = {
        "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    }
    payload= {
        "inputs": text,
        "parameters": {"candidate_labels": ["tourisme", "climat", "hôtels", "transport", "culture"]},
    }

   
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

result = prompt("Agadir est une destination très visitée...")
print(result)