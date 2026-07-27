APP_TITLE = "SINTA API"
APP_DESCRIPTION = "Backend AI SITABA"
APP_VERSION = "1.0.0"

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "gemma3:4b"


# =========================================================
# API SITABA
# =========================================================

# Data kejadian bencana umum
SITABA_NEW_DISASTER_API = (
    "https://sitaba.pu.go.id/api-public/noauth/new-disaster/"
)

# Data aset/sumber daya
SITABA_ASSET_API = (
    "https://sitaba.pu.go.id/api-public/noauth/list-assets"
)

# Data gempa bumi
SITABA_EARTHQUAKE_API = (
    "https://sitaba.pu.go.id/api-public/public/list-gempa-bumi/"
)


# =========================================================
# CORS FRONTEND LOKAL
# =========================================================

ALLOWED_ORIGINS = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
    "http://localhost:5501",
    "http://127.0.0.1:5501",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

EXPORT_DIR = "exports"