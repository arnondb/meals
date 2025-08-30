import random

# Generate random number
secret_number = random.randint(1, 100)


# Your code goes here
def guess():
  clue = ""
  attempts = 0
#    print(secret_number)
  while True:
    guess = input(f"Guess a number between {1} and {100} {clue} ")
    number = int(guess)
    attempts += 1
    if number > secret_number:
        clue = f"(less than {number})"
    elif number < secret_number:
        clue = f"(greater than {number})"
    else:
        break  
  print(f"You guessed it! The secret number is {number}")   
  print("It took you", (attempts), "attempts to guess") 
guess()
  
  	