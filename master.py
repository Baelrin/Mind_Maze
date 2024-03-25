import random
import sys
from enum import Enum


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3


TOP_OF_RANGE = {Difficulty.EASY: 10, Difficulty.MEDIUM: 100, Difficulty.HARD: 1000}


def print_message(message, color_code=None):
    if color_code and sys.platform != "win32":
        print(f"\033[{color_code}m{message}\033[0m")
    else:
        print(message)


def get_user_input(prompt, min_value=1):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value and min_value != 0:
                print_message("Please type a number larger than 0 next time.", 31)
                continue
            return value
        except ValueError:
            print_message("Please type a number next time.", 31)


def select_difficulty():
    while True:
        print("Select difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        choice = get_user_input("Your choice: ")
        if choice in [1, 2, 3]:
            return choice
        print_message("Invalid choice. Please select a number between 1 and 3.", 31)


def main():
    difficulty = Difficulty(select_difficulty())
    top_of_range = TOP_OF_RANGE[difficulty]

    random_number = random.randint(1, top_of_range)
    guesses = 0

    while True:
        guesses += 1
        user_guess = get_user_input("Make a guess: ")

        if user_guess == random_number:
            print_message("You got it!", 32)
            break
        elif user_guess > random_number:
            print_message("Nope! You were above the number!", 33)
        else:
            print_message("Nope! You were below the number!", 33)

    print(f"You got it in {guesses} guesses")


if __name__ == "__main__":
    main()
