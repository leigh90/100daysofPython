import os
from art import logo
all_bids = {}

print(logo)
def auction():
    price_bids = []
    for bids in all_bids:
        price_bids.append(all_bids[bids])
    print(price_bids)
    print(max(price_bids))
    max_bid = max(price_bids)
    for bids in all_bids:
        if max_bid == all_bids[bids]:
            print(f'the highest bidder is {bids} bidding Ksh {all_bids[bids]}')

def add_bidders():
    other_bidders = True

    while other_bidders:
        user_name = input('What is your name? ')
        user_bid = int(input('How much are you bidding? '))
        all_bids[user_name]=user_bid
        print(all_bids)
        should_continue = input("Are there are other bidders? Yes or No ").lower()
        if should_continue == 'no':
            other_bidders = False
            auction()
        else:
            os.system('clear')
    
   





add_bidders()
