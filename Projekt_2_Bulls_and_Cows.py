#projekt_2.py: Druhý projekt do Engeto Online Python Akademie
#author: Michal Kavan
#email: kavan1@centrum.cz
#discord: Michal K.#5207

import random
digit_count = 4
LINE = "-"*50


def print_welcome_message():
    pozdrav = f"""Hi there!
{LINE}
I've generated a random {digit_count}-digit number for you.
         Let's play a bulls and cows game.
{LINE}"""
    print(pozdrav)

def generate_secret_number():
      first_digit = random.choice(range(1, 9))
      remaining_digits = [random.randint(0, 9) for _ in range(digit_count - 1)]
      digits = [first_digit] + remaining_digits
      random_number = ''.join(map(str, digits))
      return int(random_number)

def get_user_guess():
    while True:
        guess = input(f"Enter a number:\n{LINE}\n>>> ")
        if len(guess) != digit_count or not guess.isdigit():
            print(f"Invalid input. Please enter a {digit_count}-digit number.")
        elif guess[0] == '0':
            print(f"Invalid input. {digit_count}-digit number cannot start with 0")
        else:
            return int(guess)

def pluralize(word, count):
    if count == 1:
        return word
    else:
        return word + 's'

def compare_numbers(secret_number, user_guess):
    secret_str = str(secret_number)
    user_str = str(user_guess)
    bulls = sum(user_str[i] == secret_str[i] for i in range(digit_count))
    cows = sum(user_str[i] in secret_str for i in range(digit_count)) - bulls
    return bulls, cows

def play_game():
    print_welcome_message()
    attempts = 0
    while True:
        user_guess = get_user_guess()
        attempts += 1
        bulls, cows = compare_numbers(secret_number, user_guess)
        bulls_word = pluralize("bull", bulls)
        cows_word = pluralize("cow", cows)
        print(f"{bulls} {bulls_word}, {cows} {cows_word}")
        if bulls == digit_count:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break

secret_number = generate_secret_number()
play_game()
