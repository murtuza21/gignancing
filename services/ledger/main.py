from __future__ import annotations

import os
from datetime import datetime
from typing import Dict

from fastapi import Depends, FastAPI, Header, HTTPException

from services.common.analytics import track
from services.common.demo import DEMO_USERS
from services.common.security import UserRole, audit, get_audit_logs, require_role
from services.schemas import LoanCreate, LoanRead, RepaymentCreate, RepaymentRead

DEMO_MODE = os.getenv("DEMO_MODE") == "true"

app = FastAPI(title="Ledger Service")

_loans: Dict[int, LoanRead] = {}
_repayments: Dict[int, RepaymentRead] = {}
_idempotency_keys: set[str] = set()

if DEMO_MODE:
    users = list(DEMO_USERS.values())
    for idx, u in enumerate(users, start=1):
        loan = LoanRead(
            id=idx,
            user_id=u["id"],
            principal=u["max_principal"],
            interest_rate=5.0,
            term_months=6,
            status="disbursed",
            created_at=datetime.utcnow(),
        )
        _loans[idx] = loan
        repayment = RepaymentRead(
            id=idx,
            loan_id=idx,
            amount=loan.principal / 6,
            due_date=datetime.utcnow(),
            paid_at=datetime.utcnow(),
        )
        _repayments[idx] = repayment


@app.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/loans", response_model=LoanRead)
def create_loan(
    payload: LoanCreate,
    idempotency_key: str = Header(None),
    role: UserRole = Depends(require_role(UserRole.UNDERWRITER, UserRole.ADMIN)),
) -> LoanRead:
    if idempotency_key and idempotency_key in _idempotency_keys:
        raise HTTPException(status_code=409, detail="Duplicate request")
    loan_id = len(_loans) + 1
    loan = LoanRead(
        id=loan_id,
        user_id=1,
        status="pending",
        created_at=datetime.utcnow(),
        **payload.dict(),
    )
    _loans[loan_id] = loan
    if idempotency_key:
        _idempotency_keys.add(idempotency_key)
    audit("create_loan", user_id=1, endpoint="/loans", meta=str(loan_id))
    track("loan_disbursed", {"loan_id": loan_id})
    return loan


@app.get("/loans", response_model=list[LoanRead])
def list_loans(
    role: UserRole = Depends(require_role(UserRole.SUPPORT, UserRole.ADMIN))
) -> list[LoanRead]:
    return list(_loans.values())


@app.get("/loans/{loan_id}", response_model=LoanRead)
def get_loan(loan_id: int) -> LoanRead:
    loan = _loans.get(loan_id)
    if not loan:
        raise HTTPException(status_code=404, detail="Loan not found")
    return loan


@app.post("/repayments", response_model=RepaymentRead)
def create_repayment(
    payload: RepaymentCreate,
    role: UserRole = Depends(
        require_role(UserRole.USER, UserRole.SUPPORT, UserRole.ADMIN)
    ),
) -> RepaymentRead:
    repayment_id = len(_repayments) + 1
    repayment = RepaymentRead(id=repayment_id, paid_at=None, **payload.dict())
    _repayments[repayment_id] = repayment
    audit(
        "create_repayment",
        user_id=1,
        endpoint="/repayments",
        meta=str(repayment_id),
    )
    track("repayment_success", {"repayment_id": repayment_id})
    return repayment


@app.post("/stripe/webhook")
def stripe_webhook() -> dict[str, str]:
    return {"status": "received"}


@app.get("/audit")
def audit_logs(role: UserRole = Depends(require_role(UserRole.ADMIN))):
    return [a.action for a in get_audit_logs()]
