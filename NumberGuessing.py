# Number guessing game a.k.a HiLo
# The player enters a number. The program says whether the number to be guessed
# is higher or lower than the user's guess.
# This continues until the player guesses the right number

import random

number = random.randint(-100, 100)
attempt = 1
guess = 101
while (guess != number):
    try:
        guess = int(input("Enter your guess: "))
        while (guess != number):
            if (number > guess):
                print("Number is greater than your guess. Aim higher")
                guess = int(input("Enter your guess: "))
            elif (number < guess):
                print("Number is smaller than your guess. Aim lower")
                guess = int(input("Enter your guess: "))
            attempt += 1
        print("Congralutions! You've guessed the number right! You have made ",
              attempt, " attempts")
    except(TypeError, ValueError, NameError):
        print("Error! You must enter an integer number only")
