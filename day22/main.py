from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

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
scoreboard = Scoreboard()

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

    # detect collision with up and  down walls
    if ball.ycor() > 330 or ball.ycor() < -350:
        ball.wall_bounce()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) <50 and ball.xcor() < -340:
        ball.paddle_bounce()

    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect Left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()
