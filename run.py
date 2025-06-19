# Import random module to generate a random number
import random

''' This is a Python Number Guessing Game.
This game generates a random number between 1 and 15,
and prompts the user to guess the number.
User tries to guess the number, and the game provides feedback. '''

def game_rule():
    ''' This function prints the game rules to the user '''
    print("\n" + "=" * 50)
    print("Welcome to the Number Guessing Game. Have fun!")
    print("NUMBER GUESSING GAME - RULES".center(50))
    print ("=" * 50)
    print("The rules are simple:")
    print("1. I will think of a number between 1 and 15.")
    print("2. You have to guess the number.")
    print("3. I will give you hints if your guess is too high or too low.")
    print("4. You must enter numbers only between 1 and 15.")
    print("5. Repeating the same number will result in invalid attempts.")
    print("6. Try to guess the number in as few attempts as possible.")
    print("=" * 50 + "\n")

game_rule()




'''
def play_again():
    # prompt the user to check if they want to play again
    response = input("Would you like to play again? (yes/no):\n")
    # create a logic condition to check what to do
    if response == "yes" or response == "Yes" or response == "YES":
        game()
    else:
        print("Thank you for playing!")
        return


# create a game function
def game():
    # create a variable to keep tract of the number of attempts guessed
    of_guessed = 0
    correct_guess = False

    # Welcome the user to the game
    print("Welcome to the Number Guessing Game. Have fun!")

    # initiate random numbers and assign it to a variable
    guess_number = random.randint(1, 15)

    # Guess user input that prompts the user to guess a number
    print("Guess a number between 1 and 15:\n")
    # Create a WHile loop that keep running  for guessing
    while correct_guess == False:
        # run this Try/ Except block to catch errors
        try:
            # Ask the user to guess a number
            user_guess = int(input("Enter your Guess:\n"))
        except Exception as e:
            print(f"An error occurred. Game Over!!")
            return
        # initiate a logic to check the guess
        if user_guess < guess_number:
            print("Your guess is too low. Try again!")
            # increment the number of attempts guessed
            of_guessed += 1

        elif user_guess > guess_number:
            print("Your guess is too high. Try again!")
            of_guessed += 1

        elif user_guess == guess_number:
            of_guessed += 1
            print(f"Correct! It's {guess_number}, you got it in {of_guessed} attempts.")
            # set the correct guess to True to end the loop
            correct_guess = True

        # Call the play again function
    play_again()


# Game function call

game()
'''