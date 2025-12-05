import os
from dotenv import load_dotenv



load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
HF_TOKEN=os.getenv("HF_TOKEN")
GEMINI_key=os.getenv("GEMINI_KEY")


