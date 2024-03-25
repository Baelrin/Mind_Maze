import random
from enum import Enum
import sys


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


TOP_OF_RANGE = {Difficulty.EASY: 10, Difficulty.MEDIUM: 100, Difficulty.HARD: 1000}


def print_colored(message, color_code):
    if sys.platform == "win32":
        print(message)
    else:
        print(f"\033[{color_code}m{message}\033[0m")


def get_user_input(prompt, min_value=1):
    while True:
        try:
            value = int(input(prompt))
            if value <= min_value:
                print_colored("Please type a number larger than 0 next time.", 31)
                continue
            return value
        except ValueError:
            print_colored("Please type a number next time.", 31)


def select_difficulty():
    print("Select difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = get_user_input("Your choice: ")
    if choice not in [1, 2, 3]:
        print_colored("Invalid choice. Please select a number between 1 and 3.", 31)
        return select_difficulty()
    return choice


def main():
    difficulty = Difficulty(select_difficulty())
    top_of_range = TOP_OF_RANGE[difficulty]

    random_number = random.randint(1, top_of_range)
    guesses = 0
    game_over = False

    while not game_over:
        guesses += 1
        user_guess = get_user_input("Make a guess: ")

        if user_guess == random_number:
            print_colored("You got it!", 32)
            game_over = True
        elif user_guess > random_number:
            print_colored("Nope! You were above the number!", 33)
        else:
            print_colored("Nope! You were below the number!", 33)

    print(f"You got it in {guesses} guesses")


if __name__ == "__main__":
    main()
