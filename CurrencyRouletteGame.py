import requests
import random
from Utilities import is_valid_input

API_KEY = '9043a5b0-732a-11ec-aa73-e596fc0f3f89'
BASE_CURRENCY = 'USD'
URL = f"https://freecurrencyapi.net/api/v2/latest?apikey={API_KEY}&base_currency={BASE_CURRENCY}"

g_difficulty = 0
g_rand_number = random.randint(1, 100)
g_min_interval = 0
g_max_interval = 0
g_user_guess = 0


def get_money_interval():
    global g_min_interval, g_max_interval
    res = requests.get(URL).json()
    usd_to_ils = res['data']['ILS']
    total_value = usd_to_ils * g_rand_number
    g_min_interval = total_value - (5 - g_difficulty)
    g_max_interval = total_value + (5 - g_difficulty)


def get_guess_from_user():
    global g_user_guess
    g_user_guess = is_valid_input(f"What do you think the value of {g_rand_number} will be from USD to ILS: ")


def is_in_intervals():
    if g_min_interval < g_user_guess < g_max_interval:
        return True
    return False


def play(difficulty):
    global g_difficulty
    g_difficulty = difficulty
    get_money_interval()
    get_guess_from_user()
    return is_in_intervals()

