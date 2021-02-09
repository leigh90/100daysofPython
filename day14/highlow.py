from gamedata import data
from art import logo
import random

# print(data[0]['name'])
# print(data[0]['follower_count'])
# print(data[0]['description'])
# print(data[0]['country'])



# shuffle the list each time the game begins
choice_a = random.choice(data)
choice_b = random.choice(data)
# print(data)
# compare two elements in the order they appear
if data[0]['follower_count'] > data[1]['follower_count'] :
    print(f"follower count one is {data[0]['follower_count']} and follower count two is {data[1]['follower_count']}")

# playerguess
# playerguess = input(" Choose 'A' or 'B': ").upper()
follower_list = []
# for i in data:
#     follower_list.append(i['follower_count'])
#     # print(i['follower_count'])


# COMPARE FOLLOWER_COUNTS
# for i in data:
#     follower_list.append(i['follower_count'])
#     for num in range(len(follower_list)-1):
#         if follower_list[num] > follower_list[num + 1]:
#             print(f'{follower_list[num]} Go for Houston')
#         else:
#             print(f"{follower_list[num]} NOPE")
# print(follower_list)  

    




# for entity in enumerate(data):
#     print(entity)



