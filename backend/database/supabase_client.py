import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL:
    raise ValueError("SUPABASE_URL belum diisi pada file .env")

if not SUPABASE_KEY:
    raise ValueError("SUPABASE_KEY belum diisi pada file .env")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def get_supabase() -> Client:
    return supabase


def test_connection():
    try:
        result = (
            supabase
            .table("visitors")
            .select("*")
            .limit(1)
            .execute()
        )

        return {
            "status": True,
            "message": "Supabase Connected",
            "rows": len(result.data or [])
        }

    except Exception as e:
        return {
            "status": False,
            "message": str(e)
        }


if __name__ == "__main__":
    print(test_connection())