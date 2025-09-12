import os
from enum import Enum

from dotenv import load_dotenv


class CurrencyUnit(Enum):
    RIAL = "ریال"
    TOMAN = "تومان"
    HEZAR_TOMAN = "هزار تومان"


def get_env_variable(key, env_path=None) -> None:
    if env_path is None:
        env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    load_dotenv(env_path)
    return os.getenv(key)
