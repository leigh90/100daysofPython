from gamedata import data
from art import logo, vs
import random
import os 


score = 0
game_should_continue = True


# format account data 

def format_data(account ):
    """
    Format account data into a printable format
    """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name} {account_descr} {account_country}"

account_b = random.choice(data)

while game_should_continue:
    # generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers 'A' or 'B': ").lower()
    os.system('clear')
    print(logo)

    def check_anwer(guess, a_followers,b_followers):
        """
        Take user guess and follower counts and returns if they got it right
        """
        if a_followers > b_followers:
            # if guess == 'a':
            #     return True
            # else:
            #     return False
            # OR these are the same
            return guess == 'a'
        else:
            return guess == "b"



    # check user answer
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b["follower_count"]
    is_correct = check_anwer(guess, a_follower_count, b_follower_count)
    if is_correct:  
        print("Right-O")
    else:
        print("Wrong, Danny boy")

    # keep track of the score
    score = 0
    if is_correct:
        score += 1
        print(f"Your score is {score}")
    else:
        game_should_continue = False
        print(f'sorry, your score is {score}')
        