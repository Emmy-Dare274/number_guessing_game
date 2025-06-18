# Number Guessing Game


<strong> Number Guessing Game </strong> is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

It is a game developed with the excitement of gambling and predicting winning numbers just like betting. It challenges the users to guess a secret number chosen by the computer.

Users can try to predict the computer chosen number by guessing what number the computer has chosen, if they are lucky, they will guess correctly on the first attempt otherwise they keep guessing until guessed correctly.

![Number Guessing Game](assets/images/Iamresponsive.png)



[Here is the live version of my project](https://numb-guessing-game-e7bd1e907d76.herokuapp.com/)



![View of project](assets/images/numb-game-photo.png)



### How to play

This Number Guessing Game is based on the classic secret number game where the computer selects a secret number, and the user player tries to guess within number of attempts (unlimited number of attempts to make it fun) with constant feedback on whether the guess is too high or too low.

### Game Objective:
Is to guess the secret number chosen by the computer.

### Features

#### Existing Features
- Random number generation
    - Computer randomly choose a secret number
    - The player cannot see what number the computer has chosen
    - The player guess the secret number by inputting a number
    - Accepts user input
    - Check user input and compare with computer's secret number to determine whether it's a correct guess.
    - Counts the number of user attempts to guess the number

- Input validation and error-checking
    - A user must enter a number
    - You cannot enter letters, strictly numbers
    - Game over if anything aside number is input
    - Prompt user whether they like to play again by input yes or no
    - If chose `no` the game is aborted with a thank you message




- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

