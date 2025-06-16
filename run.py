# Import random module to generate a random number
import random

# declare a variable to generate a random number
guess_number = random.randint(1, 15)
# print("Random number generated:", guess_number)

# create a game function and the play again function

try:
    # Ask the user to guess a number
    print("Welcome to the Number Guessing Game!")
    user_guess = int(input("Guess a number between 1 and 15:\n"))
    print(f'Your guess is: {user_guess}')
    print("Correct guess is:", guess_number)
except Exception as e:
    print(f"An error occurred. Invalid input!")
    print("Please enter a valid integer between 1 and 15.")

