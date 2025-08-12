from typing import Any, Dict, List

from pydantic import BaseModel


class AgentState(BaseModel):
    user_query: str
    next_action: str = "planner"
    steps: List[str] = []
    meta_data: Dict[str, str] = {}
    pdf_names: List[str] = []
    summary: str = ""
    memory: List[Dict[str, Any]] = []
