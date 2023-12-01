from .models.state import StateRequest
from .models.phone_number import PhoneNumberRequest
from .config import TOKEN
from .api import OnlimeSimAPIClient


client = OnlimeSimAPIClient(TOKEN)
balance = client.get_balance()
print(balance)

number_phone = client.get_phone_number(PhoneNumberRequest(
    service="dns-shop"
))
print(number_phone)

state = client.get_state(StateRequest(
    tzid=number_phone.tzid
))
print(state)
