# SCOPE
# LOCAL SCOPE when a variable is defined within a function and cannot be accessed outside of it.
# GLOBAL SCOPE when a variable is defined ouside any function and can be accessed anywhere by any function

# How to modify glabally scoped variables
enemies = 10

def increase_enemies():
    enemies += 1 #if you were to run this you will get an error telling you that the local variable enemeies was referenced before assignment. this is because python thinks that you are trying to modify a new variable without creating and assigning it first.instead use the global keyword instead to reference the global enemies you created.
    print(f'enemies inside function {enemies}')

increase_enemies()
print(f"enenmies outside function: {enemies}")


# the global keyword allows you to modify global variables. this isnt always a great idea.
def increase_enemies():
    global enemies
    enemies += 1 
    print(f'enemies inside function {enemies}')

increase_enemies()
print(f"enenmies outside function: {enemies}")

# GLOBAL CONSTANTS
# Create these and name these using uppercase letters and this will help python know and auto complete them for you as well as helping you know not to change them
PI = 3.14159
URL = 'https://www.google.com'
TWITTER_HANDLE = '@adler_1044'