# # add
# def add(n1,n2):
#     return n1 + n2
# # subtract
# def subtract(n1,n2):
#     return n1 - n2
#
# # multiply
# def multiply(n1,n2):
#     return n1 * n2
#
# # divide
# def divide(n1,n2):
#     return n1 // n2
#
# TODO Functions are considered first class objects can be passed around as arguments
# # higher order functions that can call other functions within themselves and execute them
# def calculator(n1,n2,func):
#     return func(n1,n2)
#
# result = calculator(4,5,multiply)
# print(result)
#
# # # todo nested Functions
# def outer_funcion():
#     print('Im outer')
#
#     def nestedfunction():
#         print('Im inner')
#
#     nestedfunction()
#
# outer_funcion()
#
# # todo Functions can be returned from other functions
# def outer_function():
#     print('Im outer')

#     def nestedfunction():
#         print('Im inner')

#     return nestedfunction

# # outer_function()
# #all this does is print the outer function
# new_var = outer_function()
# # new_var now refers to the nested function
# # print(type(outer_function))
# new_var()
# print(type(new_var))

# TODO PYTHON DECORATORS
# a decorator wraps another function either modifying it or adding to its functionality
import time

def decorator_function(function):
    def wrapper_function():
        time.sleep(5)
        function()
    return wrapper_function

@decorator_function
def say_hello():
    print('Ssup boo')

def say_bye():
    print('Bye')

@decorator_function
def say_greeting():
    print('Hello love')

say_hello()
say_bye()
say_greeting()
# todo the @decorator is basically syntactic sugar for passing in the function to another function and then assigning it to a variable
# decorated_var = decorator_function(say_greeting)
# decorated_var()