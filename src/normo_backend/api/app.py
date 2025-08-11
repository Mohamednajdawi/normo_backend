from __future__ import annotations

from fastapi import FastAPI


app = FastAPI(title="Normo Agentic Chatbot API")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
