import time
from turtle import Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    