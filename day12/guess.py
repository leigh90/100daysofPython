import random
from art import logo
print(logo)

# variables
computer_choice = random.randint(1,101)
print(computer_choice)
easy_chances = 10
hard_chances =  5 
levels = 0

# ask if the player wants a hard or easy level: if easy 10 repeat loop 10X if hard loop 5X
play_level = input("What level do you want to play on 'easy' or 'hard? " ).lower()
if play_level == 'easy':
    levels = easy_chances -1
    print('You have 10 chances')
elif play_level == 'hard':
    levels = hard_chances -1
    print('You have 5 chances ')
else:
    player_choice = input("You made and invalid choice, Please choose between 'easy' and 'hard'")

# take in a number 
player_choice = float(input("Pick a number between 1 and 100 "))

# check if the number is less or equal or more than the number generated between 1 and 100
def check_number():
    global levels
    global player_choice
    # if equal print 'mind-reader'
    if player_choice == computer_choice:
        print('Hello, You must be Wanda, cause you\'re a mind reader')
        levels = 0
    # if less print 'too low'
    elif player_choice < computer_choice:
        print(" Too low Captain America")
        levels -=1
        print(f'You now have {levels} lives left')
        player_choice = int(input("Try again: "))
    # if more print 'too high'
    else:
        print(' Over shot Iron Man, too high')
        levels -=1
        print(f'You now have {levels} lives left')
        player_choice = int(input("Try again: "))

   
while levels != 0: 
    check_number()
if levels == 0:
    print('You have run out of lives')

# easy_level = 10
# hard_level = 5

# def set_diff():
#     level = input('Choose a difficulty. Type "easy" or "hard": ').lower()
#     if level == 'easy':
#         return easy_level
#     else:
#         return hard_level

# # by creating a new variable and setting it to the function its value becomes the  output from the return of the function
# turns = set_diff()
            
# print(f'You have {turns} turns ')


    

    