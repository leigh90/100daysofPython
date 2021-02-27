from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# SETUP SCREEN
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)  # to remove the animation

# SET UP OBJECTS
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# PADDLE MOVEMENTS
screen.listen()
screen.onkey(key='m', fun=r_paddle.paddleup)
screen.onkey(key="Down", fun=r_paddle.paddledown)
screen.onkey(key='w', fun=l_paddle.paddleup)
screen.onkey(key="s", fun=l_paddle.paddledown)



game_on = True

while game_on:
    time.sleep(0.1)
    screen.update()  # this updates the screen after creating the turtle to cremove the animation
    ball.moveright()
screen.exitonclick()
