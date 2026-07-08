from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from database.supabase_client import supabase

router = APIRouter(prefix="/visitors", tags=["Visitors"])


class VisitorRequest(BaseModel):
    name: str | None = None
    nama: str | None = None
    email: str | None = None
    session_id: str | None = None
    user_agent: str | None = None


@router.post("/")
def create_visitor(data: VisitorRequest):
    name = data.name or data.nama or "-"

    payload = {
        "name": name,
        "nama": name,
        "email": data.email or "-",
        "session_id": data.session_id,
        "user_agent": data.user_agent,
        "created_at": datetime.now().isoformat()
    }

    result = supabase.table("visitors").insert(payload).execute()

    return {
        "success": True,
        "message": "Visitor berhasil disimpan",
        "data": result.data
    }


@router.get("/")
def get_visitors():
    result = (
        supabase
        .table("visitors")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    data = result.data or []

    return {
        "success": True,
        "total": len(data),
        "data": data
    }