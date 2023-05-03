from random import randint


import random
def game(x):
    guess = 0
    random_number = random.randint(1,x)
    while guess != random_number:
        guess = int(input(f"enter a number between 1 and {x} : "))
        if guess > random_number:
            print("Too high! Guess again!")
        elif guess < random_number:
            print("Too low! Guess again")
    print("Congrats! Your guess is correct")
game(10)
