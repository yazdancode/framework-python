import random

from constants import Constants


def site_url(route) -> str:
    return f"{Constants.base_url}{route}"


def assets_url(route) -> str:
    return site_url("assets/" + route)


def random_element(array):
    shuffled = array[:]
    random.shuffle(shuffled)
    return shuffled.pop()
