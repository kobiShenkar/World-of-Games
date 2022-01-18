import random
import sys
import time
from Utilities import is_valid_input

g_rand_numbers = []
g_user_numbers = []
g_difficulty = 0


def generate_sequence():
    for x in range(g_difficulty):
        g_rand_numbers.append(random.randint(1, 102))


def get_list_from_user():
    for y in range(g_difficulty):
        g_user_numbers.append(is_valid_input("Please enter a number: "))


def is_list_equal():
    if g_rand_numbers == g_user_numbers:
        return True
    return False


def play(difficulty):
    global g_difficulty
    g_difficulty = difficulty
    generate_sequence()
    print(g_rand_numbers, end='')
    time.sleep(0.7)
    sys.stdout.write('\r' + "")
    get_list_from_user()
    return is_list_equal()

