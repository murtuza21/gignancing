from pydantic import BaseModel, EmailStr


class OTPRequest(BaseModel):
    email: EmailStr | None = None
    phone: str | None = None


class OTPVerifyRequest(BaseModel):
    email: EmailStr | None = None
    phone: str | None = None
    code: str


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str


class RefreshRequest(BaseModel):
    refresh_token: str
