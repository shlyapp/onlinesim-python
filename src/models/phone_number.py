from pydantic import BaseModel, Field, validator

class PhoneNumberRequest(BaseModel):
    service: str
    country: int = Field(7)
    reject: list[str] = Field(None)
    dev_id: int = Field(None)
    number: bool = Field(True)
    lang: str = Field(None)

    
class PhoneNumberResponse(BaseModel):
    response: int
    tzid: int 
    number: str
    country: int = Field(None)
    time: int = Field(None)
    title: str = Field(None)
    response_text: str = Field(None)
