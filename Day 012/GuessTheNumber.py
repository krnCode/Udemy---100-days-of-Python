import random
from art import logo

print(logo)

HARD_MODE = 5
EASY_MODE = 10
PLAYER_GUESS = []


def cpu_number():
    cpu_choice = random.choice(range(1, 100))
    return cpu_choice
    print(f"CPU number: {cpu_choice}")  # test


def difficulty_setting():
    difficulty_selection = input(
        "Select a difficulty. \nEasy gives you 10 chances, and hard give you 5 chances.\nPress 'e' for easy and 'h' for hard: "
    )

    if difficulty_setting == "e":
        chances = EASY_MODE

    elif difficulty_setting == "h":
        chances = HARD_MODE


def player_number():
    player_choice = int(input("Choose a number between 1 to 100: "))

    if player_choice == cpu_number():
        print(
            f"You guessed right! Your number: {player_choice} - CPU number: {cpu_number()}.\nYou win!"
        )

    elif player_choice > cpu_number():
        print(f"The number is LOWER. Try again.")

    elif player_choice < cpu_number():
        print(f"The number is HIGHER. Try again.")


def compare_numbers():
    pass


start_game = input(
    "Do you want to play a game of Guess the Number? Type 'y' for yes or 'n' for no: "
)


difficulty_setting()
cpu_number()
player_number()
