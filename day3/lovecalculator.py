import re
# get user and crush names
your_name = input('What is your name? ').lower()
crush_name = input('What is your crushe\'s name? ').lower()
truelove = ['t','r','u','e','l','o','v','e']

# check how many times the members of the phrase true love appear in your names
counter1 = 0
counter2 = 0

for i in truelove:
    counter1 += (your_name.count(i))
    counter2 += (crush_name.count(i))

print(counter1)
print(counter2)

    


    
# t_count= your_name.count('t')
# r_count = your_name.count('r')
# u_count = your_name.count('u')
# e_count = your_name.count('e')
# l_count = your_name.count('l')
# o_count = your_name.count('o')
# v_count = your_name.count('v')
# e_count = your_name.count('e')

# t_count= your_name.count('t')
# r_count = crush_name.count('r')
# u_count = crush_name.count('u')
# e_count = crush_name.count('e')
# l_count = crush_name.count('l')
# o_count = crush_name.count('o')
# v_count =crush_name.count('v')
# e_count = crush_name.count('e')


# print(your_count)
# your_times = len(re.findall('[truelove]', your_name))
# crush_times = len(re.findall('[truelove]', crush_name))

# print(your_times)
# print(crush_times)

# crush_count = crush_name.count(truelove)
# print(crush_count)

# concatenate the count
# love_count = str(your_times) + str(crush_times)
# print(love_count)
love_count = str(counter1) + str(counter2)
print(love_count)
love_count_number = int(love_count)
print(love_count_number)

# return the results based on the counts
if love_count_number < 10 or love_count_number> 90:
    print(f'Your score is {love_count_number} You go together like coke and Mentos')
elif love_count_number >= 40 and love_count_number <= 50:
    print(f"Your score is {love_count_number} You're alright")
else:
    print(f'Your score is {love_count_number}')