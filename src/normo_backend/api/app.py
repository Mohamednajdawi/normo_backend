from __future__ import annotations

from fastapi import FastAPI

from normo_backend.agents.builder import graph
from normo_backend.models import AgentState

app = FastAPI(title="Normo Agentic Chatbot API")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/chat")
def chat(state: AgentState) -> AgentState:
    return graph.invoke(state)
