import random

from constants.Constants import get_env_variable


def site_url(route) -> str:
    base_url = get_env_variable("HOST")
    return f"{base_url}{route}"


def assets_url(route) -> str:
    return site_url("assets/" + route)


def random_element(array) -> str:
    shuffled = array[:]
    random.shuffle(shuffled)
    return shuffled.pop()
