from turtle import Screen
from paddle import Paddle



# SETUP SCREEN
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title('Pong')
screen.tracer(0)   # to remove the animation


# SET UP OBJECTS
paddle = Paddle()


screen.listen()
screen.onkey(key='m', fun=paddle.paddleup)
screen.onkey(key="Down", fun=paddle.paddledown)



game_on = True

while game_on:
    screen.update()  # this updates the screen after creating the turtle to cremove the animation






screen.exitonclick()