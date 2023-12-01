from pydantic import BaseModel, Field, validator, root_validator


class SetOperationOkRequest(BaseModel):
    tzid: int
    ban: int = Field(0)
    lang: str = Field("ru")


class SetOperationOkResponse(BaseModel):
    response: int
    tzid: int

    @root_validator(pre=True)
    def check_response(cls, values):
        if values.get('response') == "TRY_AGAIN_LATER":
            raise Exception("Нельзя закрыть номер, не прошло время.")
        return values
