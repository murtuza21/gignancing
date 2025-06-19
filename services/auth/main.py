from __future__ import annotations

import os
from uuid import uuid4

from fastapi import FastAPI, HTTPException

from services.common.analytics import track
from services.common.security import audit
from services.schemas import (
    OTPRequest,
    OTPVerifyRequest,
    RefreshRequest,
    TokenResponse,
)

DEMO_MODE = os.getenv("DEMO_MODE") == "true"

app = FastAPI(title="Auth Service")

_otps: dict[str, str] = {}
_refresh_tokens: dict[str, str] = {}
_public_jwk = {
    "kty": "RSA",
    "kid": "demo",
    "e": "AQAB",
    "n": "1",
}


@app.get("/healthz")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/login", response_model=dict)
def login(payload: OTPRequest) -> dict[str, bool]:
    target = payload.email or payload.phone
    if not target:
        raise HTTPException(status_code=400, detail="Email or phone required")
    code = "000000"  # demo OTP
    _otps[target] = code
    audit("send_otp", user_id=None, endpoint="/login", meta=target)
    track("platform_link_success", {"target": target})
    return {"otp_sent": True}


@app.post("/verify", response_model=TokenResponse)
def verify(payload: OTPVerifyRequest) -> TokenResponse:
    target = payload.email or payload.phone
    if not target:
        raise HTTPException(status_code=400, detail="Invalid target")
    if not DEMO_MODE and _otps.get(target) != payload.code:
        raise HTTPException(status_code=400, detail="Invalid code")
    prefix = "demo_" if DEMO_MODE else ""
    access = prefix + uuid4().hex
    refresh = prefix + uuid4().hex
    _refresh_tokens[refresh] = target
    audit("verify_otp", user_id=None, endpoint="/verify", meta=target)
    track("offer_view", {"user": target})
    return TokenResponse(access_token=access, refresh_token=refresh)


@app.post("/refresh", response_model=TokenResponse)
def refresh(payload: RefreshRequest) -> TokenResponse:
    if payload.refresh_token not in _refresh_tokens:
        raise HTTPException(status_code=400, detail="Invalid refresh token")
    prefix = "demo_" if DEMO_MODE else ""
    access = prefix + uuid4().hex
    refresh_token = prefix + uuid4().hex
    _refresh_tokens[refresh_token] = _refresh_tokens.pop(payload.refresh_token)
    return TokenResponse(access_token=access, refresh_token=refresh_token)


@app.get("/.well-known/jwks.json")
def jwks() -> dict:
    return {"keys": [_public_jwk]}


@app.post("/magic-link")
def magic_link(payload: OTPRequest) -> dict[str, bool]:
    if not payload.email:
        raise HTTPException(status_code=400, detail="Email required")
    return {"link_sent": True}
