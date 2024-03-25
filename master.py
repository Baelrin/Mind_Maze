import random


def print_colored(message, color_code):
    print(f"\033[{color_code}m{message}\033[0m")


def get_user_input(prompt, min_value=1):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
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
    return get_user_input("Your choice: ")


def main():
    difficulty = select_difficulty()
    if difficulty == 1:
        top_of_range = 10
    elif difficulty == 2:
        top_of_range = 100
    else:
        top_of_range = 1000

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
