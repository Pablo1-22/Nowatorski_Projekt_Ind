from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import os

app = FastAPI()

# Prosty model danych
class Task(BaseModel):
    name: str
    status: str = "pending"

# Przykładowa baza w pamięci (zanim podepniesz PostgreSQL w pełni)
fake_db = []

@app.get("/")
def read_root():
    # Ten endpoint przyda się do Healthchecka
    return {"message": "Aplikacja DevOps działa!"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return fake_db

@app.post("/tasks")
def add_task(task: Task):
    fake_db.append(task)
    return {"message": "Zadanie dodane", "task": task}

# Ten fragment symuluje zmienną środowiskową do połączenia z bazą
# Wymagane na ocenę 4.0 (komponent stanowy) [cite: 19]
@app.get("/db-check")
def db_check():
    db_url = os.getenv("DATABASE_URL", "Brak konfiguracji bazy")
    return {"db_connection_string": db_url}