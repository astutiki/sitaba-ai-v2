from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.supabase_client import supabase

router = APIRouter(prefix="/dashboard/chats", tags=["Dashboard Chats"])

class ChatRequest(BaseModel):
    name: str = "-"
    email: str = "-"
    question: str
    answer: str
    responseTime: int = 0
    sessionId: str = "-"

@router.post("/")
def create_chat(data: ChatRequest):
    try:
        result = (
            supabase
            .table("chat_history")
            .insert({
                "name": data.name.strip(),
                "email": data.email.lower().strip(),
                "question": data.question,
                "answer": data.answer,
                "response_time": data.responseTime,
                "session_id": data.sessionId,
                "source_type": "chatbot"
            })
            .execute()
        )

        return {
            "success": True,
            "message": "Chat berhasil disimpan.",
            "chat": result.data[0] if result.data else None
        }

    except Exception as e:
        print("ERROR CREATE CHAT:", e)
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def get_chats():
    try:
        result = (
            supabase
            .table("chat_history")
            .select("*")
            .order("created_at", desc=False)
            .execute()
        )

        rows = result.data or []

        data = []
        for row in rows:
            data.append({
                "id": row.get("id"),
                "session_id": row.get("session_id"),
                "question": row.get("question"),
                "answer": row.get("answer"),
                "intent": row.get("intent"),
                "category": row.get("category"),
                "source": row.get("source_type"),
                "waktu": row.get("created_at"),
                "time": row.get("created_at"),
                "responseTime": row.get("response_time") or 0,
                "email": row.get("email") or "-",
                "name": row.get("name") or "-"
            })

        return {
            "success": True,
            "total": len(data),
            "data": data
        }

    except Exception as e:
        print("ERROR GET CHATS:", e)
        raise HTTPException(status_code=500, detail=str(e))