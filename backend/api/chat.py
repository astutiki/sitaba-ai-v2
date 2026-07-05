from fastapi import APIRouter
from datetime import datetime
from database.supabase_client import supabase

from models.request import ChatRequest
from routers.intent_router import deteksi_intent
from routers.outscope_router import cek_out_of_scope

from routers.disaster_router import (
    proses_data_bencana,
    proses_statistik_bencana,
    proses_infrastruktur_bencana,
)

from routers.knowledge_router import proses_knowledge
from routers.resource_router import proses_resource

router = APIRouter(prefix="/chat", tags=["Chat"])


def normalize_response(result):
    if isinstance(result, dict):
        return {
            "reply": result.get("reply", ""),
            "attachments": result.get("attachments", [])
        }

    return {
        "reply": str(result),
        "attachments": []
    }


@router.post("/")
def chat(data: ChatRequest):
    user_message = data.message.strip()

    if not user_message:
        return {
            "success": False,
            "reply": "Pesan tidak boleh kosong.",
            "attachments": [],
            "timestamp": datetime.now().isoformat()
        }

    outscope = cek_out_of_scope(user_message)

    if outscope:
        return {
            "success": True,
            "reply": outscope,
            "attachments": [],
            "intent": "OUT_OF_SCOPE",
            "source": "Outscope Router",
            "timestamp": datetime.now().isoformat()
        }

    intent = deteksi_intent(user_message)

    if intent == "DISASTER":
        result = proses_data_bencana(user_message)
        source = "API SITABA"

    elif intent == "STATISTICS":
        result = proses_statistik_bencana(user_message)
        source = "API SITABA"

    elif intent == "INFRASTRUCTURE":
        result = proses_infrastruktur_bencana(user_message)
        source = "API SITABA"

    elif intent == "RESOURCE":
        result = proses_resource(user_message)
        source = "API SITABA - Sumber Daya"

    elif intent in [
        "DISASTER_IMPACT",
        "DISASTER_POTENTIAL",
        "MITIGATION",
        "PREPAREDNESS",
        "EVACUATION",
        "EMERGENCY_CONTACT",
        "FIRST_AID",
        "PUBLIC_INFORMATION",
        "FAQ",
        "GLOSSARY",
    ]:
        result = proses_knowledge(user_message, intent)
        source = "Knowledge Base"

    else:
        result = (
            "Maaf, AI SINTA belum menemukan jawaban yang sesuai. "
            "Silakan ajukan pertanyaan terkait informasi kebencanaan SITABA."
        )
        source = "Default Response"

    normalized = normalize_response(result)

    try:
        result = (
            supabase
            .table("chat_history")
            .insert({
                "session_id": getattr(data, "sessionId", None),
                "role": "user",
                "question": user_message,
                "answer": normalized["reply"],
                "category": intent,
                "intent": intent,
                "source_type": source,
                "is_success": True
            })
            .execute()
        )

        print("BERHASIL SIMPAN CHAT_HISTORY:", result.data)

    except Exception as e:
        print("ERROR SIMPAN CHAT_HISTORY:", str(e))

    return {
        "success": True,
        "reply": normalized["reply"],
        "attachments": normalized["attachments"],
        "intent": intent,
        "source": source,
        "timestamp": datetime.now().isoformat()
    }