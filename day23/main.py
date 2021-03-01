import time
from turtle import Screen
from player import Player
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# INITIALISE OBJECTS
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(key='m', fun=player.move)





game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()


screen.exitonclick()