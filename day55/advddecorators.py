class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False

    
def is_authenticated(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in == True:
            # print(args[0])
            print(type(args))
            print(args)
            print(type(__name__))
            print(__name__)
            function(args[0])
    return wrapper


@is_authenticated
def create_post(user):
    print(f"This is {user.name}'s new blog post")



def logging_decorator(fn):
    def wrapper(*args, **kwargs):
        print(f"You call {fn.__name__}{args}")
        result = fn(args[0], args[1], args[2])
        print(type(result))
        print(f"It returned: {result}") 
    return wrapper

# @logging_decorator
def name_function(a,b,c):
    print(name_function.__name__)
    return a * b * c 

name_function(1,2,3)      
    

# new_user = User('Ashley')
# new_user.is_logged_in = True
# create_post(new_user)

# EXERCISE 
