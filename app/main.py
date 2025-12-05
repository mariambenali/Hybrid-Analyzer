from app.schema import UserCreate, UserLogin
from sqlalchemy.orm import Session
from app.database import engine, get_db, Base
from app.models import User
from app.hasher import hashed_password
from fastapi import FastAPI ,Depends, HTTPException, Header
from services.config import SECRET_KEY, ALGORITHM
from services.analyzer_services import hybrd_analyzer
from fastapi.security import  HTTPBearer,HTTPBasicCredentials
from jose import jwt



Base.metadata.create_all(bind=engine)
app = FastAPI()
type_token= HTTPBearer()



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
    user_login = db.query(User).filter(user.username == User.username).first()

    if not user_login:
        raise HTTPException(status_code=404, detail="User not found")
    elif user.password != user_login.password:
        raise HTTPException(status_code=401, detail="Invalid password")
    

    payload = {"username ": user.username}
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
def analyzer(text:str):
    var = hybrd_analyzer(text)

    return var

