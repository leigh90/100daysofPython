numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)
# print(new_list)

# LIST COMPREHENSION SYNTAX 
# new_list = [(operation to achieve new_item) for item in input(the iteration could be range, for loop)]
# new_list = [new_item for item in list]

new_list = [n + 1 for n in numbers]
print(new_list)

name = 'Ashley'
newer_list = [letter for letter in name]

lister = [2, 4, 6,8]
doubled_numbers = [num * 2 for num in range(1, 5)]
print(doubled_numbers)

# Add conditional
# new_list = [new_item for item in input if test]
names = ['Alex','Beth', 'Caroline', 'Dave','Elenor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
capitalized_names = [name.upper() for name in names if len(name) > 5]
