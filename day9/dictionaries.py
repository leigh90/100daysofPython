# Key:value pair kind of like a language dictionary a word and its associated definition
# word:definition
# The syntax - {Key:Value}
# For example:
# {"Bug": "An error in a program that prevents it from running the program as expected"}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
    123: 456,
    }

# retrieving objects
# nameofdictionary['name_of_key']
print(programming_dictionary['Bug'])
print(programming_dictionary[123])



# adding new entries
programming_dictionary["Loope"] = "I havent seen this before"
print(programming_dictionary)

# add new entries to an empty dictionary
user_name = input('What is your name? ')
user_bid = int(input('How much are you bidding? '))

# all_bids = []


user_bid = {}
user_bid[user_name]=user_bid
# create an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
programming_dictionary = {} #set to empty will delete all the contents of a dictionary
print(programming_dictionary)

# edit elements of a dictionary
programming_dictionary["Loope"] = "Changed you"
print(programming_dictionary)

# looping through a dictionary
# just for keys
for thing in programming_dictionary: #thing is a variable name you can name it anything
    # to access the keys
    print(thing)
    # to add value of the keys
    print(programming_dictionary[thing])





