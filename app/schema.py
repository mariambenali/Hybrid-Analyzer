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



class Response_Analyzer(BaseModel):
    ton : str
    sumary : str
    category : str
    score : int