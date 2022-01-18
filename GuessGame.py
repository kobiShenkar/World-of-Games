import random
from Utilities import is_valid_range

secret_number = 0
g_difficulty = 0
user_guess = 0


def generate_number():
    global secret_number
    secret_number = random.randint(1, g_difficulty)


def get_guess_from_user():
    return is_valid_range(0, g_difficulty, f"Please Enter a number between 1 to {g_difficulty}: ")


def compare_results():
    if secret_number == user_guess:
        return True
    return False


def play(difficulty):
    global g_difficulty, user_guess
    g_difficulty = difficulty
    generate_number()
    user_guess = get_guess_from_user()
    return compare_results()


