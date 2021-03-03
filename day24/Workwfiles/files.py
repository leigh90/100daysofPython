# # WORIKING WITH OTHER FILES
#
# # OPENING OTHER FILES
# # Syntax -> open(filename, mode)
# # open('my_file.txt')
#
# # You can save it to a variable
# # Syntax -> variable = open(filename)
# file = open('my_file.txt')
# # READ() METHOD
# # red method returns the contents of the file as a string
# contents = file.read()
# print(contents)
# # CLOSE THE FILE
# # closing the file is important since opening the file uses up resources.
# file.close()
#
# # WITH is good because you don't have to remember to close the file
# # Syntax -> with open('filename.ext') as variablename:
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# WRITING TO THE FILE
# You have to open the file in write mode in order ti write to the file
# the write() method will absolutely overwrite the contents in the file
# with open('my_file.txt', mode='w+') as file:
#     file.write('Badass by +3')

# if all you want to do is add to the contents of the file use 'a' mode
# with open('my_file.txt', mode='a') as file:
#     file.write('I am Ashley, Python Ninja')

score = 10
newhigh_score = 3
with open('../../data.txt', mode='r') as file:
    high_score = int(file.read())
    # high_score = int(high_score)
    print(high_score)
    print(type(high_score))


with open('../../data.txt', mode="w") as file:
    if high_score < score:
        print('less thank')
        file.write(f'{newhigh_score}')



# # note that if the file you want to write to does not exist at the time of running python will create the file
# with open('new_file.txt', mode='w') as doodlydo:
#     doodlydo.write("\nI'm with her")
#     #create a new file 'new_file.txt' and writes the tect to it



#NAVIGATING FILE PATHS
# Absolute File Paths
# Starts from the root denoted by forward slash /

# Relative File Path Inside the working directory
# .dot notation means in this current directory check for...
# ./files.txt
# Say you are in day24 trying to get to files it would be
# ./Workwfiles/files.txt
# Say you are in textfiles and are trying to go up the directory
# we used to ..(two dots)
# ../example.file -> would be inside day24


