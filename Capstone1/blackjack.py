import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# when you type yes the game automatically gives you an array with 2 cards and the computer two but keeps the 2nd card hidden
# each player has an array with two cards 
# these two cards are added up, checked against 21 and the user is shown the results
# the user is then asked to either pick a new card or pass
# if the user picks a new card 
    # the cards are added to both the users and computer's array
    #  the new totals are compared and checked against 21
# if its over 21 the person



user_hand =[]
dealer_hand = []

card_pick = random.choices(cards, weights=None, k=4)
print(card_pick)

# user_hand.append(card_pick[0])
# user_hand.append(card_pick[1])
# user_hand.extend([card_pick[0],card_pick[1]])
# print(user_hand)
# dealer_hand.append(card_pick[2])
# dealer_hand.append(card_pick[2])
# dealer_hand.extend([card_pick[2],card_pick[3]])
# print(sum(dealer_hand))

def add_new_cards():
    new_card_pick = random.choice(cards)
    user_hand.append(card_pick[0])
    print(user_hand)
    dealer_hand.append(card_pick[1])
    print(dealer_hand)

def check_winner():
    if sum(user_hand) < 21:
        if sum(dealer_hand) > 21:
            print(f'You win, the dealers cards are {dealer_hand} and has {sum(dealer_hand)} and you have {user_hand} and your total is {sum(user_hand)}')
        elif sum(dealer_hand) < 21:
            if sum(user_hand) > sum(dealer_hand):
                print(f'You Win, the dealers cards are {dealer_hand} and has {sum(dealer_hand)} and you have {user_hand} and your total is {sum(user_hand)} ')
            else:
                print(f'You Lose the dealers cards are {dealer_hand} and has {sum(dealer_hand)} and you have {user_hand} and your total is {sum(user_hand)}')
    elif sum(user_hand) == 21:
            print(f'YOU WIN, you have {sum(user_hand)}')  
    elif sum(user_hand) == sum(dealer_hand):
            print(f"It's a draw")      
    else:
        print('You Lose, you have more than 21')

play = True

while play:
    user_play = input("Do you want to play a game of blackjack? Type 'y' or 'n': ")
    if user_play  == 'y':
        user_hand.extend([card_pick[0],card_pick[1]])
        print(user_hand)   
        dealer_hand.extend([card_pick[2],card_pick[3]])
        print(dealer_hand)
        print(f'You have {user_hand} and your current score is {sum(user_hand)} and the computer has {dealer_hand[0]}')
        new_card = input("Do you want to get another card? Type 'y' to get or 'n' to pass: ")
        if new_card == 'y':
            add_new_cards()
            check_winner()
            play = False
        else: 
            card_pick = random.choice(cards)
            dealer_hand.append(card_pick)
            print(card_pick)
            print(f"This is the computers hand {dealer_hand}")
            print(f" This is your hand {user_hand}")
            check_winner()
            play = False
    else: 
        play = False

    
        
        
# def deal_card():
#     card = random.choice(cards)
#     print(card)
#     return card

# # deal_card()
# # you can use a for loop to call a function a repeated number of times
# # the _ is used when you dont really need a variable there like youre not going to reference it at any point
# for _ in range(2):
#     user_cards.append(deal_card())
#     computer_cards.append(deal_card()) 

#  user_cards = []
# computer_cards = []
   
# print(user_cards)
# print(computer_cards)








