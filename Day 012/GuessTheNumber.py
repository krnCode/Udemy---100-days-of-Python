import random
from art import logo

print(logo)

HARD_MODE = 5
EASY_MODE = 10
PLAYER_GUESS = []
IS_GAME_OVER = False
DIFFICULTY_SELECTION = EASY_MODE

cpu_choice = random.choice(range(1, 100))
print(f"The number is: {cpu_choice}")  # test


def difficulty_setting():
    """Defines the difficulty setting for the game based on player input."""
    player_selection = input(
        "Select a difficulty. \nEasy gives you 10 chances, and hard give you 5 chances.\nPress 'e' for easy and 'h' for hard: "
    )

    if player_selection == "e":
        DIFFICULTY_SELECTION = EASY_MODE

    else:
        DIFFICULTY_SELECTION = HARD_MODE


def display():
    for _ in range(DIFFICULTY_SELECTION):
        PLAYER_GUESS.append("_")

    if player_choice != cpu_choice:
        print(f"Wrong guesses: {', '.join(PLAYER_GUESS) }")


def compare_numbers():
    """Compare the CPU and Player numbers and give hints."""
    if player_choice == cpu_number():
        print(
            f"You guessed right! Your number: {player_choice} - CPU number: {cpu_choice}.\nYou win!"
        )

    elif player_choice > cpu_choice:
        print(f"The number is LOWER. Try again.")

    elif player_choice < cpu_choice:
        print(f"The number is HIGHER. Try again.")


def game_start():
    """Asks Player if they want to play. If they type Y, the game starts, if they type N, the game ends."""
    start_game = input(
        "Do you want to play a game of Guess the Number? Type 'y' for yes or 'n' for no: "
    )

    if start_game == "n":
        print("Game Over.")
        IS_GAME_OVER = True

    elif start_game == "y":
        pass  # include the start of the game here


# game_start()
difficulty_setting()
player_choice = int(input("Choose a number between 1 to 100: "))
compare_numbers()
