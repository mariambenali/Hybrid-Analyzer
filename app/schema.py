from pydantic import BaseModel


class UserCreate(BaseModel):
    username : str
    password : str
    email : str



class UserLogin(BaseModel):
    username: str
    password : str

    class Config:
        model_config = {
            "from_attributes": True
            }
        

class Analyzer(BaseModel):
    text : str


class ResponseAnalyzer(BaseModel):
    ton : str
    summary : str
    category : str
    score : float

