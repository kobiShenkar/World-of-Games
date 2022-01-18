import CurrencyRouletteGame
import GuessGame
import MemoryGame
from Utilities import is_valid_range

games = [{'id': 1,
          'name': MemoryGame,
          'text': '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back'},
         {'id': 2,
          'name': GuessGame,
          'text': '2. Guess Game - guess a number and see if you chose like the computer'},
         {'id': 3,
          'name': CurrencyRouletteGame,
          'text': '3. Currency Roulette - try and guess the value of a random amount of USD in ILS'}]


def welcome(name):
    welcome_str = f"Hello {name} and welcome to the World of Games (WoG).\n"\
                  "Here you can find many cool games to play."
    return print(welcome_str)


def load_game():
    selected_game, difficulty = 0, 0
    print("Please choose a game to play:")
    for game in games:
        print(f"{game['text']}")

    selected_game = is_valid_range(0, 3, "Game number: ")
    difficulty = is_valid_range(0, 5, "Please choose game difficulty from 1 to 5: ")

    for game in games:
        if selected_game == game['id']:
            return game['name'].play(difficulty)

