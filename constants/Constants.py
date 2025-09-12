import os

from dotenv import load_dotenv


def get_env_variable(key, env_path=None)->None:
    if env_path is None:
        env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    load_dotenv(env_path)
    return os.getenv(key)
