"""
Debug API
AI SINTA
"""

from fastapi import APIRouter
from datetime import datetime
import platform
import sys
import os

from services.sitaba_service import get_bencana_terkini
from routers.intent_router import deteksi_intent

router = APIRouter(
    prefix="/debug",
    tags=["Debug"]
)


# =====================================================
# SYSTEM
# =====================================================

@router.get("/system")
def debug_system():

    return {

        "python_version": sys.version,

        "platform": platform.system(),

        "platform_release": platform.release(),

        "machine": platform.machine(),

        "working_directory": os.getcwd(),

        "timestamp": datetime.now().isoformat()

    }


# =====================================================
# SITABA API
# =====================================================

@router.get("/sitaba")
def debug_sitaba():

    try:

        data = get_bencana_terkini()

        jumlah = 0

        if isinstance(data, list):
            jumlah = len(data)

        elif isinstance(data, dict):

            for key in [
                "data",
                "results",
                "items"
            ]:

                if key in data:

                    jumlah = len(data[key])

                    break

        return {

            "status": "OK",

            "jumlah_data": jumlah,

            "timestamp": datetime.now().isoformat()

        }

    except Exception as e:

        return {

            "status": "ERROR",

            "message": str(e)

        }


# =====================================================
# INTENT
# =====================================================

@router.get("/intent")
def debug_intent(
    question: str
):

    intent = deteksi_intent(question)

    return {

        "question": question,

        "intent": intent

    }


# =====================================================
# HEALTH
# =====================================================

@router.get("/health")
def health():

    return {

        "status": "UP",

        "application": "AI SINTA",

        "version": "1.0.0",

        "timestamp": datetime.now().isoformat()

    }


# =====================================================
# ENVIRONMENT
# =====================================================

@router.get("/env")
def env():

    return {

        "cwd": os.getcwd(),

        "python": sys.executable,

        "platform": platform.platform(),

        "timestamp": datetime.now().isoformat()

    }


# =====================================================
# TEST
# =====================================================

@router.get("/test")
def test():

    return {

        "success": True,

        "message": "Debug endpoint berhasil.",

        "timestamp": datetime.now().isoformat()

    }


# =====================================================
# ALL
# =====================================================

@router.get("/all")
def debug_all():

    try:

        api = get_bencana_terkini()

        if isinstance(api, list):

            jumlah = len(api)

        elif isinstance(api, dict):

            jumlah = len(api.get("data", []))

        else:

            jumlah = 0

    except Exception:

        jumlah = 0

    return {

        "application": "AI SINTA",

        "version": "1.0.0",

        "sitaba_records": jumlah,

        "python": sys.version,

        "platform": platform.system(),

        "working_directory": os.getcwd(),

        "timestamp": datetime.now().isoformat()

    }