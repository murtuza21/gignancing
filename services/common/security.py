from __future__ import annotations

from datetime import datetime
from typing import Callable, List, Optional

from fastapi import Header, HTTPException

from .models import AuditLog, UserRole

_audit_logs: List[AuditLog] = []


def require_role(*roles: UserRole) -> Callable:
    def dependency(x_role: str = Header(...)) -> UserRole:
        try:
            role = UserRole(x_role)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid role")
        if role not in roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return role

    return dependency


def audit(
    action: str, user_id: Optional[int], endpoint: str, metadata: Optional[str] = None
) -> None:
    _audit_logs.append(
        AuditLog(
            user_id=user_id,
            action=action,
            metadata=metadata,
            created_at=datetime.utcnow(),
        )
    )


def get_audit_logs() -> List[AuditLog]:
    return _audit_logs
