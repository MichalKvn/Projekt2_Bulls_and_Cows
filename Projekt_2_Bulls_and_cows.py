#projekt_2.py: Druhý projekt do Engeto Online Python Akademie
#author: Michal Kavan
#email: kavan1@centrum.cz
#discord: Michal K.#5207

import random

def print_welcome_message():
    pozdrav = """Hi there!
-----------------------------------------------
I've generated a random 4-digit number for you.
         Let's play a bulls and cows game.
-----------------------------------------------"""
    print(pozdrav)

def generate_secret_number():
    digits = random.sample(range(1, 10), 4)
    random_number = ''.join(str(digit) for digit in digits)
    return int(random_number)

def get_user_guess():
    guess = input("Enter a number:\n-----------------------------------------------\n>>> ")
    while len(guess) != 4 or not guess.isdigit():
        print("Invalid input. Please enter a 4-digit number.")
        guess = input("Enter a number:\n-----------------------------------------------\n>>> ")
    return guess

def compare_numbers(secret_number, user_guess):
    bulls = 0
    cows = 0
    for num in range(4):
        if user_guess[num] == secret_number[num]:
            bulls += 1
        elif user_guess[num] in secret_number:
            cows += 1
    return bulls, cows

def play_game():
    secret_number = generate_secret_number()
    print_welcome_message()
    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1
        bulls, cows = compare_numbers(secret_number, user_guess)
        print(f"{bulls} bulls, {cows} cows")
        if bulls == 4:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break

play_game()
