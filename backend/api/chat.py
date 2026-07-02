from fastapi import APIRouter
from datetime import datetime

from models.request import ChatRequest
from routers.intent_router import deteksi_intent
from routers.outscope_router import cek_out_of_scope
from routers.disaster_router import (
    proses_data_bencana,
    proses_statistik_bencana,
    proses_infrastruktur_bencana,
)
from routers.knowledge_router import proses_knowledge

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/")
def chat(data: ChatRequest):
    user_message = data.message.strip()

    if not user_message:
        return {
            "success": False,
            "reply": "Pesan tidak boleh kosong.",
            "timestamp": datetime.now().isoformat()
        }

    outscope = cek_out_of_scope(user_message)
    if outscope:
        return {
            "success": True,
            "reply": outscope,
            "intent": "OUT_OF_SCOPE",
            "source": "Outscope Router",
            "timestamp": datetime.now().isoformat()
        }

    intent = deteksi_intent(user_message)

    if intent == "DISASTER":
        reply = proses_data_bencana(user_message)
        source = "API SITABA"

    elif intent == "STATISTICS":
        reply = proses_statistik_bencana(user_message)
        source = "API SITABA"

    elif intent == "INFRASTRUCTURE":
        reply = proses_infrastruktur_bencana(user_message)
        source = "API SITABA"

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
    ]:
        reply = proses_knowledge(user_message, intent)
        source = "Knowledge Base"

    else:
        reply = (
            "Maaf, AI SINTA belum menemukan jawaban yang sesuai. "
            "Silakan ajukan pertanyaan terkait informasi kebencanaan SITABA."
        )
        source = "Default Response"

    return {
        "success": True,
        "reply": reply,
        "intent": intent,
        "source": source,
        "timestamp": datetime.now().isoformat()
    }