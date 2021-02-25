from turtle import Screen
from snake2 import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Snake Ninja')
screen.tracer(0)

# CREATE A SNAKE
snake = Snake()
# CREATE FOOD
food = Food()

# CONTROL SNAKE
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
# OR
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    # delay updating the screen by 0.1 seconds
    screen.update()
    time.sleep(0.1)
    snake.move()
    # distance is a turtle method that allows you to check the distance between two turtle objects
    # in this instance the snake head and the food
    if snake.head.distance(food) < 15:
        food.refresh()





screen.exitonclick()
