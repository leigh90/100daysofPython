import random

# random_number = random.randint(100,145)
# print(random_number)
# note randint returns a whole number

random_dec = random.random()
print(random_dec)
# random.random returns a float between 0 and 1

# to get a random floating point number above 1 you cna multiply the .random() with a whole number for instance
print(random_dec * 9)

love_score = random.randint(1,100)
print(f"your love score is {love_score}")