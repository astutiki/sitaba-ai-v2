from fastapi import HTTPException, Header
from auth.user import authenticate_user
from auth.jwt_handler import create_access_token, verify_access_token


def login_user(username: str, password: str):
    user = authenticate_user(username, password)

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Username atau password salah."
        )

    token = create_access_token({
        "sub": user["username"],
        "user_id": user["id"],
        "role": user["role"],
        "fullname": user["fullname"],
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user["id"],
            "username": user["username"],
            "fullname": user["fullname"],
            "role": user["role"],
        }
    }


def get_current_user(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Silakan login terlebih dahulu."
        )

    token = authorization.replace("Bearer ", "").strip()
    payload = verify_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Token tidak valid atau sudah kedaluwarsa."
        )

    return payload