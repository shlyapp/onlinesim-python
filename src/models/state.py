from typing import List
from pydantic import BaseModel, Field, root_validator


class StateRequest(BaseModel):
    tzid: int
    message_to_code: int = Field(1)
    order_by: str = Field(None)
    msg_list: int = Field(1)
    clean: int = Field(None)
    lang: str = Field("ru")


class Message(BaseModel):
    service: str
    msg: str


class State(BaseModel):
    country: int
    sum: float
    service: str
    number: str
    werbhook_url: str = Field(None)
    response: str
    tzid: int
    time: int
    msg: List[Message] | str
    form: str
