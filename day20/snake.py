from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake Ninja')

# STEP 1: SNAKE BODY
full_snake = []
x_positions = [0, -20, -40]
for turtle_index in range(0, 3):
    new_turtle = Turtle(shape='square')
    new_turtle.color('white')
    new_turtle.penup()
    new_turtle.goto(x=x_positions[turtle_index], y=0)
    full_snake.append(new_turtle)








screen.exitonclick()
