#oop allows us write code in specialties
# models allow us to create objects with attributes(what they have)(hold plate, tables_responsible) and methods(things they can do)(take orders and payments)
# classes are blueprints to create objects

# CREATING AN OBJECT FROM A CLASS
# variable = Classname()
# car = CarBlueprint()

import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('pink')
# timmy.forward(100)
#
# # ACCESSING CLASS ATTRIBUTES
# # variable.attribute
# # car.speed
#
# my_screen = Screen()
# print(my_screen.canvheight)




# ACCESSING CLASS METHODS
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# table.field_names = ["City name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
# OR
table.add_column('POKEMON_NAME',['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('TYPE',['Electric', "Water","Fire"])
table.align = 'r'
print(table.align)
print(table)
