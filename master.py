import random


def get_user_input(prompt, min_value=1):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Please type a number larger than {min_value} next time.")
                continue
            return value
        except ValueError:
            print("Please type a number next time.")


def main():
    top_of_range = get_user_input("Type a number: ")
    random_number = random.randint(1, top_of_range)
    guesses = 0
    game_over = False

    correct_guess_message = "You got it!"
    above_message = "Nope! You were above the number!"
    below_message = "Nope! You were below the number!"

    while not game_over:
        guesses += 1
        user_guess = get_user_input("Make a guess: ")

        if user_guess == random_number:
            print(correct_guess_message)
            game_over = True
        elif user_guess > random_number:
            print(above_message)
        else:
            print(below_message)

    print(f"You got it in {guesses} guesses")


if __name__ == "__main__":
    main()
