from pathlib import Path
from threading import Lock
from typing import Literal

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/quick-chat", tags=["Quick Chat"])

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "quick_chats.json"
DATA_LOCK = Lock()

DEFAULT_ITEMS = [
    {"id": 1, "question": "Sebutkan tahun kejadian banjir di Bali?", "status": "Aktif"},
    {"id": 2, "question": "Longsor di Jawa Timur terjadi kapan?", "status": "Aktif"},
    {"id": 3, "question": "Informasi kebencanaan apa saja yang bisa dicari masyarakat melalui SITABA?", "status": "Aktif"},
]


class QuickChatCreate(BaseModel):
    question: str = Field(min_length=1, max_length=500)
    status: Literal["Aktif", "Nonaktif"] = "Aktif"


def _clean_question(value: str) -> str:
    return str(value or "").strip().replace("<", "").replace(">", "")


def _read_items() -> list[dict]:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        _write_items(DEFAULT_ITEMS)
        return [dict(item) for item in DEFAULT_ITEMS]

    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except Exception:
        _write_items(DEFAULT_ITEMS)
        return [dict(item) for item in DEFAULT_ITEMS]


def _write_items(items: list[dict]) -> None:
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    DATA_FILE.write_text(
        json.dumps(items, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


import json


@router.get("/")
def list_quick_chats():
    with DATA_LOCK:
        items = _read_items()
    return {"success": True, "total": len(items), "data": items}


@router.post("/")
def create_quick_chat(data: QuickChatCreate):
    question = _clean_question(data.question)
    if not question:
        raise HTTPException(status_code=400, detail="Pertanyaan wajib diisi.")

    with DATA_LOCK:
        items = _read_items()
        next_id = max((int(item.get("id", 0)) for item in items), default=0) + 1
        item = {"id": next_id, "question": question, "status": data.status}
        items.append(item)
        _write_items(items)

    return {"success": True, "data": item}


@router.put("/{item_id}/toggle")
def toggle_quick_chat(item_id: int):
    with DATA_LOCK:
        items = _read_items()
        item = next((row for row in items if int(row.get("id", 0)) == item_id), None)
        if item is None:
            raise HTTPException(status_code=404, detail="Quick Chat tidak ditemukan.")

        item["status"] = "Nonaktif" if item.get("status") == "Aktif" else "Aktif"
        _write_items(items)

    return {"success": True, "data": item}


@router.delete("/{item_id}")
def delete_quick_chat(item_id: int):
    with DATA_LOCK:
        items = _read_items()
        new_items = [row for row in items if int(row.get("id", 0)) != item_id]
        if len(new_items) == len(items):
            raise HTTPException(status_code=404, detail="Quick Chat tidak ditemukan.")
        _write_items(new_items)

    return {"success": True}
