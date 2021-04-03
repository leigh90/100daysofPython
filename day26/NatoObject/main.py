import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
# print(data)

nato_alphabet = pandas.DataFrame(data)
print(nato_alphabet)
all_letters= []
all_code = []

for index,row in nato_alphabet.iterrows():
    all_letters.append(row.letter)
    all_code.append(row.code)
# print(all_letters)
# print(all_code)



new_dict = {all_letters[i]: all_code[i] for i in range(len(all_letters))}
print(new_dict)

name = input('What is your name?').upper()
name_list = []
for i in name:
    print(i)
    name_list.append(i)
# print(user_input)

nato_name = {letter:code for (letter,code) in new_dict.items() if letter in name_list}
print(nato_name)

# TODO MUCH MUCHHH BETTER
phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}

word = input('Enter a word').upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)