from pydantic import BaseModel, Field


class BalanceRequest(BaseModel):
    income: bool = Field(False)
    lang: str = Field("ru")


class Balance(BaseModel):
    response: str | int
    balance: float
    zbalance: float
    
