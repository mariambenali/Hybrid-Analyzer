# Mariben-Summarizer
A fullstack application that automatically analyzes articles using two AI services.

- **Hugging Face** : Zero-Shot Classification

- **Google Gemini** : Summarization, Sentiment Analysis, and Contextual Synthesis


---

##  Project Structure

```bash
.
├── app/                    
│   ├── __init__.py
│   ├── database.py
│   ├── dockerignore
│   ├── Dockerfile
│   ├── hasher.py
│   ├── main.py             
│   ├── models.py
│   └── schema.py
│
├── hybrid-app/              
│   ├── app/
│   ├── public/
│   ├── Dockerfile
│   ├── package.json
│   ├── next.config.ts
│   ├── tailwind / postcss
│   └── README.md
│
├── services/               
│
├── docker-compose.yml      
├── .env                    
├── requirements.txt         
├── pytest.ini
└── README.md               
```


---

## Features

- Automatic article analysis

- Zero-shot text classification

- AI-generated summaries

- Tone and sentiment detection

- Secure JWT authentication

- Frontend ↔ Backend API communication

- Docker & Docker Compose support


---

## Tech Stack

### Backend

- Python

- FastAPI

- JWT Authentication

- PostgreSQL 

- Test:Mock 

### Frontend

- Next.js

- Tailwind CSS

### DevOps

- Docker

- Docker Compose


---

## Installation & Setup

### 1- Clone the repository

````
git clone https://github.com/mariambenali/Hybrid-Analyzer
cd Hybrid-Analyzer
````

### 2- Run with Docker
````
docker-compose up --build
````
- Frontend: http://localhost:3000

- Backend API: http://localhost:8000


### 3- Run without Docker

#### Backend:
````
python -m venv myvenv
source myvenv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
````

#### Frontend:
````
cd hybrid-app
npm install
npm run dev
````

---

## Testing
````
pytest
`````

---

## 👩‍💻 Author

Miriam Benali
GitHub: https://github.com/mariambenali