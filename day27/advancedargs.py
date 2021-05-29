# # todo positional arguments
#
# def myfunction(a,b,c):
#     pass
#
# myfunction(a=1,b=2, c=3)
#
# # todo  default values: call the function with default values, eliminate the need to pass in new values
# def myfunction(a=1,b=2, c=3):
#     pass
#
# myfunction()
#
# # todo change only one value
# def myfunction(a=1,b=2, c=3):
#     pass
# myfunction(b=5)
#
# # TODO Unlimited Arguments (*args): note that the word args can be replaced with any other word the key there is to use the asterisk which says accept any number of arguments passed in
# def add(*args):
#     print(args)
#     print(type(args))
#     total = 0
#     for n in args:
#         total += n
#     print(total)
#
#
# add(8,9,7,67,89,86)
#
# # TODO Keyword Arguments (**kwargs)
# def calculate(n, **kwargs):
#     print(kwargs)
#     #either
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#     #or
#     # print(kwargs['add'])
#     # print(kwargs['multiply'])
#     # prints the value of those keys
#     # this allows you to do things like
#     n += kwargs['add']
#     n *= kwargs['multiply']
#     print(n)
#     # >>>81
#
#
# calculate(3, add=6, multiply=9)

# todo this allows you to create classes with keyword arguments

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']

my_car = Car(make='Nissan', model='GT-R')
print(my_car.make)
print(my_car.model)

# say you didnt initialise one of the properties during creation, you would have an error creating instances because the class expects the two attributes to be initialised during creation of an instance you would have to use the .get() function typically used with dictionaries
# .get() returns the value of the item in the specified key
vehicle = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# dictionary.get(dictionarykey)
x = vehicle.get('model')
print(x)

# todo using .get() in this way allows you to create instances without initialising all the attributes. what it will do is set those attributes to none

class Car:
    def __init__(self, **kwargs):
        self.make= kwargs.get('make')
        self.model = kwargs.get('model')

new_car = Car(make='Ferrari')
print(new_car.model)
# >>>None

#





# TODO EXERCISE


