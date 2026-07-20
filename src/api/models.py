from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    repo_url: str


class ChatRequest(BaseModel):
    session_id: str
    question: str