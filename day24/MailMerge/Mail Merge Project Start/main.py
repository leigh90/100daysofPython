# #TODO: Create a letter using starting_letter.txt
# #for each name in invited_names.txt
# #Replace the [name] placeholder with the actual name.
# #Save the letters in the folder "ReadyToSend".
#
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
#
# import fileinput
#
# # get the names into a python list
# name_list = []
#
# with open('../../MailMerge/Mail Merge Project Start/Input/Names/invited_names.txt', 'r') as data:
#     contents = data.readlines()
#     for line in contents:
#         name_list.append(line)
# # print(name_list)
# # name_list = ['Aang', 'Zuko', 'Appa', 'Katara', 'Sokka', 'Momo', 'Uncle Iroh', 'Toph']
#
#
# # open start letter file
# letterlines = []
# with open("../../MailMerge/Mail Merge Project Start/Input/Letters/starting_letter.txt") as file:
#     letter = file.readlines()
#     # print(letter)
#
# recepient_line = []
#
# for name in range(len(name_list)):
#     for line in letter:
#         # print(line)
#         line = line.replace("[name]", name_list[name])
#         recepient_line.append(line)
# # print(recepient_line)
#
# dear_index = []
# count = 0
#
# new_letter_sub = recepient_line[1:7]
# str1 = " "
# new_letter_sub = str1.join(new_letter_sub)
# print(new_letter_sub)
# print(type(new_letter_sub))
#
# for name in range(len(name_list)):
#     with open(f'../../MailMerge/Mail Merge Project Start/Output/ReadyToSend/{name_list[name]}.txt', mode="w") as file:
#         for line in recepient_line:
#             x = recepient_line.index(line)
#             if x == 0 or x % 7 == 0:
#                 new_letter_rec = recepient_line[x]
#         file.writelines([new_letter_rec, new_letter_sub])



# ['Dear Aang\n,\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can make it!\n', '\n', 'Angela\n', 'Dear Zuko\n,\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can make it!\n', '\n', 'Angela\n', 'Dear Appa\n,\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can make it!\n', '\n', 'Angela\n', 'Dear Katara\n,\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can make it!\n', '\n', 'Angela\n', 'Dear Sokka\n,\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can make it!\n', '\n', 'Angela\n', 'Dear Momo\n,\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can make it!\n', '\n', 'Angela\n', 'Dear Uncle Iroh\n,\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can make it!\n', '\n', 'Angela\n', 'Dear Toph,\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can make it!\n', '\n', 'Angela\n']



# find the line to add the name
# add the name
# save to file with the format of letter to name


# OR
PLACEHOLDER = '[name]'
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.read()
    print(names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, name)
        print(new_letter)

with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt',mode="w") as completed_letter:
    completed_letter.write(new_letter)
