from pydantic import BaseModel, ValidationError, parse_obj_as
import requests
import json

from .config import TOKEN, MAX_ATTEMPS, DELAY
from .logger import logger

from .models.phone_number import PhoneNumberResponse, PhoneNumberRequest
from .models.set_operation_ok import SetOperationOkResponse, SetOperationOkRequest

class OnlimeSimAPI:
    def __init__(self, token: str):
        self._token = token
        self._base_url = "https://onlinesim.io/api"

    def _make_request(self, method: str, endpoint: str, data: BaseModel):
        url = f"{self._base_url}{endpoint}"
        params = data.model_dump(exclude_none=True)
        params['apikey'] = self._token
        response = requests.request(
            method=method,
            url=url,
            params=params
        ).json()

        return response

    def get_phone_number(self, data: PhoneNumberRequest) -> PhoneNumberResponse:
        endpoint = "/getNum.php"
        response = self._make_request("GET", endpoint, data)
        phone_number = PhoneNumberResponse(**response)
        print(phone_number)
        return phone_number
    
    def set_operation_ok(self, data: SetOperationOkRequest) -> SetOperationOkResponse:
        endpoint = "/SetOperationOk.php"
        response = self._make_request("GET", endpoint, data)
        set_operation_ok = SetOperationOkResponse(**response)
        return set_operation_ok
