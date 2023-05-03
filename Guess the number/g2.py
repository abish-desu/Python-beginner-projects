import random
def game(x):
    random_number = random.randint(1,x)
    guess = 0
    
    while guess != random_number:
        guess = int(input(f"Guess a number bertween 1 and {x} :"))
        if guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low")
    print("Congrats")
game(10)