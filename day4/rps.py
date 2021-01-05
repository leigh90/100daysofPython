import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


number = random.randint(0,2)
print(number)
rps_choices = [rock,paper,scissors]

# get user input and assign a choice
user_choice_number = int(input('Enter a number between 0 and 2 to select the player enter 0 for rock, 1 for paper, 2 for scissors '))
user_choice = rps_choices[user_choice_number]
# print(f'User choice is {user_choice}')

# get computer input and assign a choice
computer_choice_number = random.randint(0,2) 
computer_choice = rps_choices[computer_choice_number]
# print(f'Computer choice is {computer_choice}')

# compare user input to computer to pick a winner
if user_choice == paper:
    if computer_choice == scissors:
        print(user_choice,computer_choice)
        print('You lose')
    elif computer_choice == rock:
        print(user_choice,computer_choice)
        print('You win')
    else:
        print(user_choice,computer_choice)
        print('It\'s a draw')
elif user_choice ==scissors:
    if computer_choice == rock:
        print(user_choice,computer_choice)
        print('You lose')
    elif computer_choice == paper:
        print(user_choice,computer_choice)
        print('You win')
    else:
        print(user_choice,computer_choice)
        print('It\'s a draw')
else:
    if computer_choice == paper:
        print(user_choice,computer_choice)
        print('You lose')
    elif computer_choice == scissors:
        print(user_choice,computer_choice)
        print('You win')
    else:
        print(user_choice,computer_choice)
        print('It\'s a draw')


    






        
   