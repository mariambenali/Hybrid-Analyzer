from .gemini_services import gemini_result
from .hf_services import prompt


def hybrd_analyzer(text:str):
    hf_result = prompt(text)

    result = gemini_result(text)

    return {
        "huggingface_classification": hf_result,
        "gemini_analysis": result
    }



