# Import random module to generate a random number
import random

''' This is a Python Number Guessing Game.
This game generates a random number between 1 and 15,
and prompts the user to guess the number.
User tries to guess the number, and the game provides feedback. '''

def game_rule():
    ''' This function prints the game rules to the user '''
    print("\n" + "=" * 50)
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

#game_rule()

def game():
    ''' The Main game logic function that input validation, repeat guessing, 
    and user input handling.'''
    attempts = 0
    guessed_numbers = []
    target = random.randint(1, 15)

    print("\n" + "="*50)
    print("WELCOME TO THE NUMBER GUESSING GAME. HAVE FUN!".center(50))
    print("="*50)

    while True:
        try:
            # Get and validate user input
            user_input = input(f"\n Attempt #{attempts + 1} - Enter your guess (1-15):\n").strip()

            if not user_input:
                print("Empty input. Please enter a number between 1 and 15.")
                continue
                
            guess = int(user_input)
            # Check number range
            if guess < 1 or guess > 15:
                print("Guess out of range. Please enter a number between 1 and 15.")
                continue

            # Check for repeated guesses
            if guess in guessed_numbers:
                print(f"You have already guessed {guess}. Try a different number.")
                continue
            # Check valid new guess
            attempts += 1
            guessed_numbers.append(guess)

            # Provide feedback on the guess
            if guess < target:
                print(f"{guess} is too low. Try again!")
            elif guess > target:
                print(f"{guess} is too high. Try again!")
            else:
                print("\n" + "="*50)
                print(f"CONGRATULATIONS! You guessed {target} correctly!")
                print(f"It took you {attempts} attempt{'s' if attempts > 1 else ''}.")
                print("="*50)
                return
            
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 15.")
                

game()






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

'''