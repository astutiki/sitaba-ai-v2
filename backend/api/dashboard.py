"""
Dashboard API
AI SINTA
"""

from fastapi import APIRouter
from datetime import datetime

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary():
    return {
        "success": True,
        "title": "Dashboard AI SINTA",
        "data": {
            "total_chat": 0,
            "total_user": 0,
            "total_feedback": 0,
            "total_export": 0,
            "total_api_request": 0,
            "success_rate": "0%",
            "average_response_time_ms": 0
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
    return {
        "success": True,
        "data": [
            "Bencana hari ini apa saja?",
            "Statistik bencana bulan Juni 2026 apa?",
            "Ruas jalan apa yang terdampak bencana?",
            "Bagaimana mitigasi banjir?",
            "Nomor darurat bencana apa?"
        ],
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
            "database": "UNKNOWN"
        },
        "timestamp": datetime.now().isoformat()
    }