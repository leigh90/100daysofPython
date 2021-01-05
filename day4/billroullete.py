import random
# get users names
people = input('Please enter your names in separated by a comma and a space. ')
# create a list
people_list = people.split(',')
print(people_list)
# get the length of the list and use it to generate the random number
numberlimit = len(people_list)
print(numberlimit)
# let the random number choose who pays the bill
random_number = random.randint(0,numberlimit-1)
print(random_number)
bill_payer = people_list[random_number]
print(f'{bill_payer} will pay the bill. ')