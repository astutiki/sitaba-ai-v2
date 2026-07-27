from __future__ import annotations

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = ROOT_DIR / "backend"

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

from backend.main import app as backend_app


class StripApiPrefixMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope.get("type") in {"http", "websocket"}:
            path = scope.get("path", "")

            if path == "/api":
                scope["path"] = "/"
                scope["raw_path"] = b"/"

            elif path.startswith("/api/"):
                new_path = path[4:] or "/"
                scope["path"] = new_path
                scope["raw_path"] = new_path.encode("utf-8")

        await self.app(scope, receive, send)


app = StripApiPrefixMiddleware(backend_app)