############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# the range function takes the last parameter upto but not including it so 20 will be excluded.

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# it goes out of range because even though there are 6 objects we count from 0 so once it gets to 5 6 is out of the index range
# fix by using (len(dice_imgs)) as the upper bound of randint dice_num = randint(1, len(dice_imgs))

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# nothing happens for 1994 because its not included you need an equals operator

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
#     print("You can drive at age {age}.")
# convert age to integer
# use f-string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(pages)
# print(word_per_page)
# print(total_words)
# the issue was the double equal sign

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1,2,3,5,8,13])