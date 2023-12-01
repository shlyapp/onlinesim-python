import requests
from pydantic import BaseModel

from .logger import logger

from .models.phone_number import PhoneNumber, PhoneNumberRequest
from .models.operation import OperationOkResponse, OperationOkRequest
from .models.balance import Balance, BalanceRequest
from .models.state import State, StateRequest


class OnlimeSimAPIClient:
    def __init__(self, token: str):
        self._token = token
        self._base_url = "https://onlinesim.io/api"
        logger.info(f"Create OnlimeSimAPIClient with token {token}")

    def _make_request(self, method: str, endpoint: str, data: BaseModel):
        url = f"{self._base_url}{endpoint}"
        logger.info(f"Send {method} request\nurl: {url}\ndata: {data}")
        params = data.model_dump(exclude_none=True)
        params['apikey'] = self._token
        response = requests.request(
            method=method,
            url=url,
            params=params
        ).json()
        logger.info(f"Get answer from request:\n{response}")

        return response

    def get_phone_number(self, data: PhoneNumberRequest) -> PhoneNumber:
        endpoint = "/getNum.php"
        response = self._make_request("GET", endpoint, data)
        phone_number = PhoneNumber(**response)
        return phone_number
    
    def set_operation_ok(self, data: OperationOkRequest) -> OperationOkResponse:
        endpoint = "/SetOperationOk.php"
        response = self._make_request("GET", endpoint, data)
        set_operation_ok = OperationOkResponse(**response)
        return set_operation_ok

    def get_state(self, data: StateRequest):
        endpoint = "/getState.php"
        response = self._make_request("GET", endpoint, data)
        try:
            state = State(**response[0])
            return state
        except:
            raise Exception("Number not exist")
            
    def get_balance(self, data: BalanceRequest = BalanceRequest()) -> Balance:
        endpoint = "/getBalance.php"
        response = self._make_request("GET", endpoint, data)
        balance = Balance(**response)
        return balance

