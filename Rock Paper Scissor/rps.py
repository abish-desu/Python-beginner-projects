import random

def play():
    user = input("enter your choice : 'r' for rock,\
    's' for scissor ,'p' for paper ::")
    computer = random.choice(['r','p','s'])
    print("Computer choosed " + computer)

    if user == computer:
        return"It's a tie !"

    # r>p , p>r , s>p
    if is_win(user , computer):                  # user, player * computer, opponent
        return'You won'

    return'you lost'

def is_win(player , opponent):                   # condition to win
        # r>s , p>r , s>p
    if (player =='r' and opponent =='s') or (player =='s' and opponent =='p') or \
    (player =='p' and opponent =='r'):
        return True
    
print(play())