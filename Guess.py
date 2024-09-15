"""
Practicing: random library

"""
import random

def guess(x):
    random_number = int(random.randint(0, x))
    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))

        if guess < random_number:
            print("Sorry, guess again. Too low!")
        elif guess > random_number:
            print("Sorry, guess again. Too high!")

    print(f"Congratulations! You have guessed the number {guess}")


# Creating looping to repeat the process

run = True 

while run:
    limit = int(input(f"Insert the upper limit for this round: "))
    guess(limit)

    run = int(input (f"To end the game press 0. \n"))
    