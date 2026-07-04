from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database.supabase_client import supabase

router = APIRouter(prefix="/visitors", tags=["Visitors"])


class VisitorRequest(BaseModel):
    name: str
    email: str


@router.post("/")
def create_visitor(data: VisitorRequest):
    try:
        existing = (
            supabase.table("visitors")
            .select("*")
            .eq("email", data.email)
            .execute()
        )

        if existing.data:
            return {
                "success": True,
                "message": "Visitor sudah ada.",
                "visitor": existing.data[0]
            }

        result = (
            supabase.table("visitors")
            .insert({
                "name": data.name,
                "email": data.email
            })
            .execute()
        )

        return {
            "success": True,
            "message": "Visitor berhasil disimpan.",
            "visitor": result.data[0] if result.data else None
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/")
def get_visitors():
    try:
        result = (
            supabase.table("visitors")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        return {
            "success": True,
            "total": len(result.data or []),
            "data": result.data or []
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))