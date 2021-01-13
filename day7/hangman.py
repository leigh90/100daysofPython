import random
# select a random word from a list
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

# create a blank spaces for the chosen word
blank_word = []
for i in range(len(chosen_word)):
    blank_word.append("_")
print(blank_word)

# ask for user input and check the input against our word
user_letter = input('Guess a letter: ').lower()
for char in chosen_word:
    if user_letter == char:
        print("right")
    else:
        print("Wrong")
# get the indexes to replace the blank sentence
index_list = []
for index in range(len(chosen_word)):
    if chosen_word[index] == user_letter:
        index_list.append(index)
        print(index) 
print(index_list)

# replace the letters 
# while "_" not in blank_word:
for index in index_list:
    for i in blank_word:
        blank_word[index] = user_letter
print(blank_word)




    

    

