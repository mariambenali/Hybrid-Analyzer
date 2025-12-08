from .database import Base
from sqlalchemy import String,Integer, Column, Float



class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)



class AnalysisLog(Base):
    __tablename__ = "analysis_logs"
    
    id= Column(Integer,primary_key=True)
    ton = Column(String)
    summary = Column(String)
    category = Column(String)
    score = Column(Float)



    