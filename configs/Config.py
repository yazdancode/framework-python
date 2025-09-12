import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BASE_URL = os.getenv("HOST", "http://localhost:5000/")
