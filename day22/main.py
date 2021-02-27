from turtle import Screen
from paddle import Paddle

# SETUP SCREEN
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)  # to remove the animation

# SET UP OBJECTS
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(key='m', fun=r_paddle.paddleup)
screen.onkey(key="Down", fun=r_paddle.paddledown)
screen.onkey(key='w', fun=l_paddle.paddleup)
screen.onkey(key="s", fun=l_paddle.paddledown)

game_on = True

while game_on:
    screen.update()  # this updates the screen after creating the turtle to cremove the animation

screen.exitonclick()
