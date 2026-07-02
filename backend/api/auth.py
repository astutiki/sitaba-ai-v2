from fastapi import APIRouter, HTTPException
from datetime import datetime
import secrets

from models.request import LoginRequest

router = APIRouter(prefix="/auth", tags=["Auth"])

TOKENS = set()

USERS = {
    "admin": {
        "password": "admin123",
        "role": "admin",
        "fullname": "Administrator"
    },
    "sinta": {
        "password": "sitaba123",
        "role": "user",
        "fullname": "User SINTA"
    }
}


@router.post("/login")
def login(data: LoginRequest):
    username = data.username.strip()
    password = data.password.strip()

    if username not in USERS:
        raise HTTPException(status_code=401, detail="Username atau password salah.")

    user = USERS[username]

    if user["password"] != password:
        raise HTTPException(status_code=401, detail="Username atau password salah.")

    token = secrets.token_hex(32)
    TOKENS.add(token)

    return {
        "success": True,
        "message": "Login berhasil.",
        "token": token,
        "username": username,
        "fullname": user["fullname"],
        "role": user["role"],
        "timestamp": datetime.now().isoformat()
    }


@router.post("/logout")
def logout(token: str):
    if token in TOKENS:
        TOKENS.remove(token)

    return {
        "success": True,
        "message": "Logout berhasil.",
        "timestamp": datetime.now().isoformat()
    }


def cek_token(token: str):
    if token not in TOKENS:
        raise HTTPException(status_code=401, detail="Token tidak valid atau belum login.")
    return True