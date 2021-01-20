# # declaring the function syntax
# def my_function_name():
#     # do something
#     print("It was nice to nice to know ya lets do it again")

# my_function_name()
# # calling the function

# # functions with inputs
# def my_function_with_name(name):
#     # do this with 123
#     # then do this
#     name = 'Ashley'
#     # name(parameter) = 'Ashley'(argument)
#     # parameter = the variable
#     # argument = the actual piece of data, actual value of the data
#     print(f'Hey {name}')

# my_function_with_name('Ashley')
# so whatever value we pass in when we call the function is passed to the function
# the placeholder or variable name 'something'. so the value of something is now 123

# POSITIONAL VS KEYWORD ARGUMENTS
# function with inputs
name = input('Hello')
location = input('Where do you live?')
def greet_with(name,location):
    print(f'Hello {name} ')
    print(f'What is it like in {location}? ')
    
greet_with(name,location)
# you can add as many inputs as you like
# remember you must maintain the order so thet the correct parameter is assigned to the correct value. 
# this is a positional argument. the comp will assign the values in the  order you supplied them

#KEYWORD
def greet_with(name,location):
    print(f'Hello {name} ')
    print(f'What is it like in {location}? ')
    
greet_with(name='Tessa',location='Nairobi')
# note you can now order these as you wish since it will adhere to the assignments you give it

