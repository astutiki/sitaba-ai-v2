from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config import (
    APP_TITLE,
    APP_DESCRIPTION,
    APP_VERSION,
    ALLOWED_ORIGINS,
)

from backend.api.chat import router as chat_router
from backend.api.auth import router as auth_router
from backend.api.debug import router as debug_router
from backend.api.dashboard import router as dashboard_router
from backend.api.visitor import router as visitor_router
from backend.api.chat_history import router as chat_history_router
from backend.api.export import router as export_router
from backend.api.quick_chat import router as quick_chat_router
from backend.routers.statistics_chart_router import router as statistics_chart_router


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
app.include_router(dashboard_router)
app.include_router(visitor_router)
app.include_router(chat_history_router)
app.include_router(export_router)
app.include_router(quick_chat_router)
app.include_router(statistics_chart_router)


@app.get("/")
def home():
    return {
        "message": "SINTA API berjalan.",
        "status": "ok",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "backend.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )