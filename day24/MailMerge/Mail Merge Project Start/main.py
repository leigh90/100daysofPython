#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# get the names into a python list
name_list = []

# with open('../../MailMerge/Mail Merge Project Start/Input/Names/invited_names.txt', 'r') as data:
#     contents = data.readlines()
#     for line in contents:
#         name_list.append(line)
# print(name_list)
name_list = ['Aang', 'Zuko', 'Appa', 'Katara', 'Sokka', 'Momo', 'Uncle Iroh', 'Toph']

# replace the opening line
with open('../../MailMerge/Mail Merge Project Start/Input/Letters/starting_letter.txt', 'r') as form_letter:
    for name in range(len(name_list)):
        line_one = form_letter.readline()
        lineone = line_one.replace("[name]", name_list[name])
        print(line_one)

with open('../../MailMerge/Mail Merge Project Start/Input/Letters/starting_letter.txt','a') as startletter:
    startletter.write(line_one)




# find the line to add the name

# add the name
# save to file with the format of letter to name

































































# lineones = []
# with open('../../MailMerge/Mail Merge Project Start/Input/Letters/starting_letter.txt', mode='r') as formletter:
#     line_one = formletter.readline()
#     for name in range(len(name_list)-1):
#         line_one = line_one.replace('[name]', name_list[name])
#         lineones.append(line_one)


# for name in range(len(name_list)-1):
#     with open(f'../../MailMerge/Mail Merge Project Start/Output/ReadyToSend/{name_list[name]}.txt','w') as write_letter:
#         write_letter.write





#
# txt = "I like bananas"
# for num in range(0,6):
#     txt = txt.replace('bananas',name_list[num], len(name_list))
#     print(txt)





