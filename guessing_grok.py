import random

# Generate random number
secret_number = random.randint(1, 100)

def guess():
    clue = ""
    attempts = 0
    while True:
        try:
            guess = input(f"Guess a number between 1 and 100 {clue}: ")
            number = int(guess)
            if number < 1 or number > 100:
                print("Please enter a number between 1 and 100.")
                continue
            attempts += 1
            if number > secret_number:
                clue = f"(less than {number})"
            elif number < secret_number:
                clue = f"(greater than {number})"
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
            continue
    print(f"You guessed it! The secret number is {number}.")
    print(f"It took you {attempts} attempts to guess.")

guess()