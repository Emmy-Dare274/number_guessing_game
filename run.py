# Import random module to generate a random number
import random

# declare a variable to generate a random number
# guess_number = random.randint(1, 15)

# create a function to play again

def play_again():
    # prompt the user to check if they want to play again
    response = input("Would you like to play again? (yes/no):\n")
    # create a logic condition to check what to do
    if response == "yes" or response == "Yes" or response == "YES" or response == "y" or response == "Y":
        game()
    else:
        print("Thank you for playing!")
        return

# create a game function and the play again function



# create a game function

def game():
    # create a variable to keep tract of the number of attempts guessed
    attempts_guessed = 0
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
            #print(f'Your guess is: {user_guess}')
            #print("Correct guess is:", guess_number)
        except Exception as e:
            print(f"An error occurred. Game Over!!")
            return
        # initiate a logic to check the guess
        if user_guess < guess_number:
            print("Your guess is too low. Try again!")
            # increment the number of attempts guessed
            attempts_guessed += 1

        elif user_guess > guess_number:
            print("Your guess is too high. Try again!")
            attempts_guessed += 1

        elif user_guess == guess_number:
            attempts_guessed += 1
            print(f"Congratulations! The correct guess was {guess_number} and you guessed it in {attempts_guessed} attempts.")
            # set the correct guess to True to end the loop
            correct_guess = True








# Game function call

game()
