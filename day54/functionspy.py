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
# # higher order functions that can call other functions within themselves and execute them
# def calculator(n1,n2,func):
#     return func(n1,n2)
#
# result = calculator(4,5,multiply)
# print(result)
#
# # todo nested Functions
def outer_funcion():
    print('Im outer')

    def nestedfunction():
        print('Im inner')

    nestedfunction()

outer_funcion()

# todo Functions can be returned from other functions
def outer_function():
    print('Im outer')

    def nestedfunction():
        print('Im inner')

    return nestedfunction

new_var = outer_function()
print(type(outer_function))
new_var()
# print(type(new_var))


