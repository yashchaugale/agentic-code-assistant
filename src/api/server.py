from fastapi import FastAPI

app = FastAPI(
    title="RepoMind API",
    version="1.0"
)


@app.get("/")
def home():

    return {
        "message": "Welcome to RepoMind 🚀"
    }