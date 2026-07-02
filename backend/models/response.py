from pydantic import BaseModel
from typing import Optional


class ChatResponse(BaseModel):
    success: bool = True
    reply: str
    source: Optional[str] = None
    timestamp: Optional[str] = None


class LoginResponse(BaseModel):
    success: bool
    token: str
    username: str


class ErrorResponse(BaseModel):
    success: bool = False
    message: str