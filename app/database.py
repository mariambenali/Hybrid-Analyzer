from fastapi import FastAPI
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import session_maker
from sqlalchemy.ext.declarative import declarative_base
import os


load_dotenv()

DATABASE_URL = os.getenv("DATABASE")

engine= create_engine(DATABASE_URL)

SessionLocal= session_maker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
