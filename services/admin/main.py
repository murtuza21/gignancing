from __future__ import annotations

from functools import wraps

from fastapi import Depends, FastAPI, HTTPException, Request

app = FastAPI(title="Admin Gateway")


def get_role(request: Request) -> str:
    return request.headers.get("X-Role", "user")


def require_role(role: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, role_name: str = Depends(get_role), **kwargs):
            if role_name.lower() != role:
                raise HTTPException(status_code=403, detail="forbidden")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def audit(action: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # placeholder for audit log
            return func(*args, **kwargs)

        return wrapper

    return decorator


@app.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/admin/users", dependencies=[Depends(require_role("admin"))])
@audit("list_users")
def list_users() -> list:
    return []
