from fastapi import APIRouter
from database.supabase_client import supabase

router = APIRouter(tags=["Dashboard"])


@router.get("/visitors/")
def get_visitors():
    try:
        response = (
            supabase
            .table("visitor")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        data = response.data or []

        return {
            "success": True,
            "source_table": "visitor",
            "total": len(data),
            "data": data
        }

    except Exception as e:
        return {
            "success": False,
            "source_table": "visitor",
            "error": str(e),
            "total": 0,
            "data": []
        }


@router.get("/dashboard/chats/")
def get_dashboard_chats():
    try:
        response = (
            supabase
            .table("chat_history")
            .select("*")
            .order("created_at", desc=True)
            .execute()
        )

        data = response.data or []

        normalized = []

        for item in data:
            normalized.append({
                "id": item.get("id"),
                "name": item.get("name") or item.get("nama") or item.get("visitor_name"),
                "email": item.get("email") or item.get("visitor_email"),
                "question": item.get("question") or item.get("message") or item.get("user_message") or item.get("pertanyaan"),
                "answer": item.get("answer") or item.get("reply") or item.get("bot_response") or item.get("jawaban"),
                "response_time": item.get("response_time") or item.get("responseTime") or 0,
                "created_at": item.get("created_at") or item.get("waktu") or item.get("time")
            })

        return {
            "success": True,
            "source_table": "chat_history",
            "total": len(normalized),
            "data": normalized
        }

    except Exception as e:
        return {
            "success": False,
            "source_table": "chat_history",
            "error": str(e),
            "total": 0,
            "data": []
        }


@router.get("/dashboard/summary/")
def get_dashboard_summary():
    try:
        visitor = (
            supabase
            .table("visitor")
            .select("*")
            .execute()
        )

        chats = (
            supabase
            .table("chat_history")
            .select("*")
            .execute()
        )

        visitor_data = visitor.data or []
        chat_data = chats.data or []

        unique_email = {
            str(x.get("email") or "").lower().strip()
            for x in visitor_data
            if x.get("email")
        }

        return {
            "success": True,
            "title": "Dashboard AI SINTA",
            "data": {
                "total_user_unik": len(unique_email),
                "total_login": len(visitor_data),
                "total_chat": len(chat_data),
                "today_chat": len(chat_data),
                "average_response_time_ms": 0,
                "total_feedback": 0,
                "total_export": 0,
                "total_api_request": len(chat_data),
                "success_rate": "100%"
            }
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }