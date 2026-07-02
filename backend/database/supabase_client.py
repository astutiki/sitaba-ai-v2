"""
===========================================================
SUPABASE CLIENT
AI SITABA
===========================================================
"""

import os

from supabase import create_client, Client
from dotenv import load_dotenv

# ==========================================================
# Load .env
# ==========================================================

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
# ==========================================================
# Validasi Environment
# ==========================================================

if not SUPABASE_URL:
    raise ValueError(
        "SUPABASE_URL belum diisi pada file .env"
    )

if not SUPABASE_KEY:
    raise ValueError(
        "SUPABASE_KEY belum diisi pada file .env"
    )

# ==========================================================
# Membuat Client
# ==========================================================

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# ==========================================================
# Helper
# ==========================================================

def get_supabase() -> Client:
    """
    Mengembalikan object Supabase Client.
    """

    return supabase


# ==========================================================
# Test Koneksi
# ==========================================================

def test_connection():

    try:

        result = (
            supabase
            .table("statistics")
            .select("*")
            .limit(1)
            .execute()
        )

        return {
            "status": True,
            "message": "Supabase Connected",
            "rows": len(result.data)
        }

    except Exception as e:

        return {
            "status": False,
            "message": str(e)
        }


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    print(test_connection())