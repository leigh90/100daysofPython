#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# get the names into a python list
name_list = []

with open('../../MailMerge/Mail Merge Project Start/Input/Names/invited_names.txt', 'r') as data:
    contents = data.readlines()
    for line in contents:
        name_list.append(line)
print(name_list)
# name_list = ['Aang', 'Zuko', 'Appa', 'Katara', 'Sokka', 'Momo', 'Uncle Iroh', 'Toph']


# open each file

# find the line to add the name
# add the name
# save to file with the format of letter to name