from pydantic import BaseModel


class ScoreRequest(BaseModel):
    earnings: list[float]
    rating: float
    tenure_months: int


class ScoreResponse(BaseModel):
    tier: str
    max_principal: float
