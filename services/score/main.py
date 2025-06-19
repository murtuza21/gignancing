from __future__ import annotations

import os
from math import exp

from fastapi import FastAPI, HTTPException

from services.common.demo import DEMO_USERS
from services.schemas import ScoreRequest, ScoreResponse

DEMO_MODE = os.getenv("DEMO_MODE") == "true"

app = FastAPI(title="Score Service")


def _logistic(x: float) -> float:
    return 1 / (1 + exp(-x))


def _predict(score: ScoreRequest) -> ScoreResponse:
    avg_earnings = sum(score.earnings) / len(score.earnings)
    val = 0.001 * avg_earnings + 0.5 * score.rating + 0.05 * score.tenure_months
    prob = _logistic(val)
    if prob > 0.8:
        tier = "A"
        max_principal = 5000.0
    elif prob > 0.5:
        tier = "B"
        max_principal = 2500.0
    else:
        tier = "C"
        max_principal = 1000.0
    return ScoreResponse(tier=tier, max_principal=max_principal)


@app.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/demo/user/{email}", response_model=ScoreRequest)
def demo_user(email: str) -> ScoreRequest:
    if email in DEMO_USERS:
        u = DEMO_USERS[email]
        return ScoreRequest(
            earnings=u["earnings"],
            rating=u["rating"],
            tenure_months=u["tenure_months"],
        )
    raise HTTPException(status_code=404, detail="Not found")


@app.post("/score", response_model=ScoreResponse)
def score(payload: ScoreRequest) -> ScoreResponse:
    return _predict(payload)
