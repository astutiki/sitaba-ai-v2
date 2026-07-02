from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.chat import router as chat_router
from api.auth import router as auth_router
from api.debug import router as debug_router

from config import (
    APP_TITLE,
    APP_DESCRIPTION,
    APP_VERSION,
    ALLOWED_ORIGINS,
)

app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(debug_router)


@app.get("/")
def home():
    return {
        "message": "SINTA API berjalan.",
        "status": "ok"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }