# DRAW A SPIROGRAPH

from turtle import Turtle, Screen
import random
timmy = Turtle()

# turtle.home()
# timmy.position()(0.00,0.00)
# turtle.heading()
for n in range(0,361,10):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    # return color
    timmy.circle(100)
    timmy.left(n)
    timmy.circle(100)

timmy.speed('fastest')








screen = Turtle.Screen()
screen.exitonclick()