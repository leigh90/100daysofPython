from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake Ninja')
screen.tracer(0)

# CREATE A SNAKE
snake = Snake()
# CONTROL SNAKE
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_on = True
while game_on:
    # delay updating the screen by 0.1 seconds
    screen.update()
    time.sleep(0.1)

    snake.move()






screen.exitonclick()
