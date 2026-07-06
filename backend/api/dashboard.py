"""
Dashboard API
AI SINTA
"""

from fastapi import APIRouter
from datetime import datetime, date
from database.supabase_client import supabase

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary():
    try:
        visitor_result = (
            supabase
            .table("visitor")
            .select("*")
            .execute()
        )

        chat_result = (
            supabase
            .table("chat_history")
            .select("*")
            .execute()
        )

        visitors = visitor_result.data or []
        chats = chat_result.data or []

        unique_emails = set()
        for visitor in visitors:
            email = (visitor.get("email") or "").lower().strip()
            if email:
                unique_emails.add(email)

        today = date.today().isoformat()

        today_chats = [
            chat for chat in chats
            if str(chat.get("created_at", "")).startswith(today)
        ]

        response_times = []
        for chat in chats:
            value = chat.get("response_time")
            if value is not None:
                try:
                    response_times.append(float(value))
                except:
                    pass

        avg_response = (
            sum(response_times) / len(response_times)
            if response_times else 0
        )

        return {
            "success": True,
            "title": "Dashboard AI SINTA",
            "data": {
                "total_user_unik": len(unique_emails),
                "total_login": len(visitors),
                "total_chat": len(chats),
                "today_chat": len(today_chats),
                "average_response_time_ms": round(avg_response, 2),
                "total_feedback": 0,
                "total_export": 0,
                "total_api_request": len(chats),
                "success_rate": "100%" if chats else "0%"
            },
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        return {
            "success": False,
            "title": "Dashboard AI SINTA",
            "error": str(e),
            "data": {
                "total_user_unik": 0,
                "total_login": 0,
                "total_chat": 0,
                "today_chat": 0,
                "average_response_time_ms": 0,
                "total_feedback": 0,
                "total_export": 0,
                "total_api_request": 0,
                "success_rate": "0%"
            },
            "timestamp": datetime.now().isoformat()
        }


@router.get("/ai-usage")
def dashboard_ai_usage():
    return {
        "success": True,
        "data": {
            "total_prompt": 0,
            "total_tokens": 0,
            "total_success": 0,
            "total_error": 0,
            "model": "gemma3:4b"
        },
        "timestamp": datetime.now().isoformat()
    }


@router.get("/popular-questions")
def popular_questions():
    try:
        result = (
            supabase
            .table("chat_history")
            .select("question")
            .execute()
        )

        rows = result.data or []

        counter = {}

        for row in rows:
            q = (row.get("question") or "").strip()
            if q:
                counter[q] = counter.get(q, 0) + 1

        sorted_questions = sorted(
            counter.items(),
            key=lambda item: item[1],
            reverse=True
        )

        data = [
            {
                "question": question,
                "total": total
            }
            for question, total in sorted_questions[:10]
        ]

        return {
            "success": True,
            "data": data,
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        return {
            "success": False,
            "data": [],
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }


@router.get("/intent-statistics")
def intent_statistics():
    return {
        "success": True,
        "data": {
            "DISASTER": 0,
            "STATISTICS": 0,
            "INFRASTRUCTURE": 0,
            "MITIGATION": 0,
            "EVACUATION": 0,
            "EMERGENCY_CONTACT": 0,
            "OUT_OF_SCOPE": 0
        },
        "timestamp": datetime.now().isoformat()
    }


@router.get("/system-status")
def system_status():
    return {
        "success": True,
        "system": {
            "api": "UP",
            "sitaba_api": "UNKNOWN",
            "ollama": "UNKNOWN",
            "database": "UP"
        },
        "timestamp": datetime.now().isoformat()
    }