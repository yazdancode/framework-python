import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)

base_url = os.getenv("BASE_URL")
pi = float(os.getenv("PI"))
mode = os.getenv("MODE")
db = os.getenv("DB")
