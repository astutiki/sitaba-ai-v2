from auth.password import hash_password, verify_password

USERS_DB = {
    "admin": {
        "id": 1,
        "username": "admin",
        "fullname": "Administrator",
        "role": "admin",
        "password": hash_password("admin123"),
        "is_active": True,
    },
    "sinta": {
        "id": 2,
        "username": "sinta",
        "fullname": "User SINTA",
        "role": "user",
        "password": hash_password("sitaba123"),
        "is_active": True,
    },
}


def get_user(username: str):
    return USERS_DB.get(username)


def authenticate_user(username: str, password: str):
    user = get_user(username)

    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    if not user.get("is_active"):
        return None

    return user