import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = str(os.getenv("TOKEN"))
MAX_ATTEMPS = 7
DELAY = 10
