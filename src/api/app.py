import uuid

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.models import AnalyzeRequest, ChatRequest
from api.session_store import SessionStore
from engine.engine import RepoMindEngine

store = SessionStore()

app = FastAPI(
    title="RepoMind API",
    version="1.0.0"
)

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create one engine instance
engine = RepoMindEngine()


@app.get("/")
def home():
    return {
        "message": "Welcome to RepoMind API"
    }


@app.post("/analyze")
def analyze(request: AnalyzeRequest):
    # Create a new engine for each analyzed repository
    engine = RepoMindEngine()

    result = engine.analyze(request.repo_url)

    session_id = str(uuid.uuid4())

    store.save(session_id, engine)

    return {
        "success": True,
        "session_id": session_id,
        "analysis": result
    }


@app.post("/chat")
def chat(request: ChatRequest):
    engine = store.get(request.session_id)

    if engine is None:
        return {
            "success": False,
            "error": "Invalid session_id"
        }

    return engine.ask(request.question)