# todo positional arguments

def myfunction(a,b,c):
    pass

myfunction(a=1,b=2, c=3)

# todo  default values: call the function with default values, eliminate the need to pass in new values
def myfunction(a=1,b=2, c=3):
    pass

myfunction()

# todo change only one value
def myfunction(a=1,b=2, c=3):
    pass
myfunction(b=5)

# TODO Unlimited Arguments (*args): note that the word args can be replaced with any other word the key there is to use the asterisk which says accept any number of arguments passed in
def add(*args):
    print(args)
    print(type(args))
    total = 0
    for n in args:
        total += n
    print(total)


add(8,9,7,67,89,86)


