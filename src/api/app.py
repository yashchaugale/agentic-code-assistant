

import uuid

from fastapi import FastAPI

from api.models import AnalyzeRequest, ChatRequest
from api.session_store import SessionStore
from engine.engine import RepoMindEngine

store = SessionStore()

app = FastAPI(
    title="RepoMind API",
    version="1.0.0"
)

engine = RepoMindEngine()


@app.get("/")
def home():
    return {
        "message": "Welcome to RepoMind API"
    }

@app.post("/analyze")
def analyze(request: AnalyzeRequest):

    engine = RepoMindEngine()

    result = engine.analyze(request.repo_url)

    session_id = str(uuid.uuid4())

    store.save(session_id, engine)

    return {
        "session_id": session_id,
        "analysis": result
    }

@app.post("/chat")
def chat(request: ChatRequest):
    engine = store.get(request.session_id)

    if engine is None:
        return {
            "error": "Invalid session_id"
        }

    answer = engine.ask(request.question)

    return {
        "answer": answer
    }