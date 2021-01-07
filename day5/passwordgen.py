import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
allcharacters = [letters,numbers,symbols]

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
# new_pass_list = []

# # easy
# # get number of letters append to list
# random_letter_list = []
# for i in range(0,nr_letters):
#     n = random.randint(0,len(letters)-1)
#     random_letter_list.append(n)
# print(random_letter_list)

# # get characters and create a string
# letter_list = []
# for i in random_letter_list:
#     letter_list.append(letters[i])
#     new_pass_list.append(letters[i])
#     new = ''.join(letter_list)
# print(letter_list)
# print(new)

# # get number of numbers append to list
# random_number_list = []
# for i in range(0,nr_numbers):
#     n = random.randint(0,len(numbers)-1)
#     random_number_list.append(n)
# print(random_number_list)

# number_list = []
# for i in random_number_list:
#     number_list.append(numbers[i])
#     new_pass_list.append(numbers[i])
#     new_number = ''.join(number_list)
# print(number_list)
# print(new_number)

# # get number of symbols and append to list
# random_symbol_list = []
# for i in range(0,nr_symbols):
#     n = random.randint(0,len(symbols)-1)
#     random_symbol_list.append(n)
# print(random_symbol_list)

# symbol_list = []
# for i in random_symbol_list:
#     symbol_list.append(symbols[i])
#     new_pass_list.append(symbols[i])
#     new_symbols = ''.join(symbol_list)
# print(symbol_list)
# print(new_symbols)

# print(f'this is new pass list {new_pass_list}')
# newest = random.shuffle(new_pass_list)
# print(''.join(new_pass_list))
# new_password = new + new_number + new_symbols

# print(f'Your new password is {new_password}')

chosen = random.choice(letters)
print(chosen)

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")

# print(password_list)