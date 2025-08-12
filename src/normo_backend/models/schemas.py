from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

Role = Literal["system", "user", "assistant", "tool"]


class ChatMessage(BaseModel):
    role: Role
    content: str
    tool_name: Optional[str] = None
    tool_args: Optional[dict] = None


class ChatRequest(BaseModel):
    messages: list[ChatMessage] = Field(default_factory=list)
    user_id: Optional[str] = None
    stream: bool = False


class ChatResponse(BaseModel):
    message: ChatMessage
