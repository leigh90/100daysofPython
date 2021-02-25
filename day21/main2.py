from turtle import Screen
from snake2 import Snake
from food import Food
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

# CONTROL SNAKE
screen.listen()
screen.onkey(key="m", fun=snake.up)
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

    # FOOD COLLISION
    # distance is a turtle method that allows you to check the distance between two turtle objects in this instance the snake head and the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # DETECT WALL COLLISION
    if snake.head.xcor() > 280  or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

#     DETECT TAIL COLLISION
#     for segment in snake.segments:
#         if segment == snake.head:
#             pass
#         elif snake.head.distance(segment) < 10:
#             game_on = False
#             scoreboard.game_over()

    # OR
    # everything except the head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()








screen.exitonclick()
