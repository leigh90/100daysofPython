from turtle import Turtle, Screen
import random

screen = Screen()
# sets screen width and height
screen.setup(width=600,height=500)

is_race_on = False
user_answer = screen.textinput(title="Choose your Turtle", prompt="Which turtle will win the race? Enter a color: ")
print(user_answer)
colors = ['red','indigo','yellow','blue','orange', 'green', 'blue']
y_positions = [180, 150, 110, -80, -50, -20]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-280,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_answer:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >270:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_answer:
                print(f'Winner winner, chicken dinner the winning color is {winning_color}')
            else:
                print(f'SOrry mate the winning colour is {winning_color} you sleep with the dishes today!')
        rand_distance =  random.randint(0,10)
        turtle.forward(rand_distance)

    
screen.exitonclick()