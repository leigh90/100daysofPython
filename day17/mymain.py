# CREATING CLASSES
# class User:
#     # classes named with PascalCase
#     pass

#You can add attributes to objects like this without having explicitly declared them in advance. however its not resuable since you have to do it over and over for other objects you create
# userone = User()
# userone.id = "001"
# userone.username = "angela"


# class User:
    # def __init__(self):
    #     print("new user being created")

    # __init__ function is called everytime you create an object using the class.
# usertwo = User()
# usertwo.id = "001"
# usertwo.username = "ashley"
# print(usertwo.username)

# ading attributes to classes. passed in via init method. tbject to be created with the needed attributes. his allows the o

# class Car:
#     def __init__(self, seats):
#         self.seats = seats
#         print("new user being created")
#
#     def enter_race_mode(self):
#         self.seats = 2
#
#
# mycar = Car(5)
# print(mycar.seats)
# mycar.enter_race_mode()
# print(mycar.seats)

class User:
    def __init__(self, user_id, username):
        #         by convention the parameter is the same as the attribute name
        self.id = user_id
        self.username = username
        #when you have an attribute with a default value you dont have to pass it into the init method thats just wasteful
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


userfour = User(2, 'Helena')
user_three = User(1, 'dwight')
userfour.follow(user_three)
print(user_three.username)
print(user_three.id)
print(userfour.followers)
print(userfour.following)
print(user_three.followers)
print(user_three.following)


