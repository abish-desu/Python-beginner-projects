import random

def guess_game(x):
    random_number =random.randint(1,x)            # generate random number
    guess = 0
    while guess != random_number:                 # to enter loop guess = 0
        guess = int(input(f"enter a number between 1 and {x} :"))
        if guess  < random_number:
            print("Guess again!! Too Low!!")
        elif guess > random_number:
            print("Guess again!! Too high!!")

    # if number is guessed loop breaks and ... 
                          
    print("congratulation! You have guessed correctly")     
guess_game(10)
    
        
    


