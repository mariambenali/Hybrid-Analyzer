from app.schema import UserCreate, UserLogin ,ResponseAnalyzer, Analyzer
from sqlalchemy.orm import Session
from app.database import engine, get_db, Base
from app.models import User, AnalysisLog
from app.hasher import hashed_password, verify_password
from fastapi import FastAPI ,Depends, HTTPException
from services.config import SECRET_KEY, ALGORITHM
from services.gemini_services import hybrd_analyzer
from fastapi.security import  HTTPBearer,HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
from jose import jwt
import json




Base.metadata.create_all(bind=engine)
app = FastAPI()
type_token= HTTPBearer()

origins = [
    "http://localhost:3000", 
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/register")
def register(user:UserCreate, db: Session = Depends(get_db)):
    hash_password = hashed_password(user.password)
    new_user = User(username=user.username,
                    password = hash_password,
                    email = user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.post("/login")
def login(user:UserLogin , db:Session = Depends(get_db)):
    user_login = db.query(User).filter(User.username == user.username).first()

    if not user_login:
        raise HTTPException(status_code=404, detail="User not found")
    elif not verify_password(user.password, user_login.password):
        raise HTTPException(status_code=401, detail="Invalid password")
    

    payload = {"username": user.username}
    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

    return token
    

@app.get("/token")
def get_token(token:HTTPBasicCredentials = Depends(type_token)):
    try:
        decoded= jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return decoded
    
    except Exception as e:
        raise HTTPException(status_code=401, detail="Verify Token")
    
@app.post("/analyzer")
def analyzer(payload: Analyzer, db: Session = Depends(get_db)):
    data = hybrd_analyzer(payload.text)  

    newdata =AnalysisLog(
        summary = data.summary,
        ton = data.ton,
        score = data.score,
        category = data.category,
    )
    db.add(newdata)
    db.commit()
    db.refresh(newdata)

    return newdata