from gemini_services import TourismFactor, TourismAnalysis
from hf_services import prompt



def hybrd_analyzer(text:str):
    hf_result = prompt(text)

    gemini_result = (TourismFactor, TourismAnalysis(text))

    return {
        "huggingface_classification": hf_result,
        "gemini_analysis": gemini_result
    }



