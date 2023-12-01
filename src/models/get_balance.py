from pydantic import BaseModel, Field


class GetBalanceRequest(BaseModel):
    income: bool = Field(False)
    lang: str = Field("ru")


class GetBalanceResponse(BaseModel):
    response: str | int
    balance: float
    zbalance: float
    
