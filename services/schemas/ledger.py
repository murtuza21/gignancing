from datetime import datetime

from pydantic import BaseModel


class LoanCreate(BaseModel):
    principal: float
    interest_rate: float
    term_months: int


class LoanRead(LoanCreate):
    id: int
    user_id: int
    status: str
    created_at: datetime


class RepaymentCreate(BaseModel):
    loan_id: int
    amount: float
    due_date: datetime


class RepaymentRead(RepaymentCreate):
    id: int
    paid_at: datetime | None = None
