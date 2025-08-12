from typing import Dict, List

from pydantic import BaseModel


class AgentState(BaseModel):
    user_query: str
    memory: List[Dict[str, str]]
    next_action: str = "planner"
    steps: List[str] = []
    meta_data: Dict[str, str] = {}
    summary: str = ""
    pdf_names: List[str] = []
