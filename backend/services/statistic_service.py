from database.supabase_client import get_supabase

db = get_supabase()

result = (
    db
    .table("statistics")
    .select("*")
    .execute()
)