from turtle import Turtle
import time
import random
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        # super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Create car instances
        """
        random_chance = random.randint(1, 6) #this manages the frequency of generating a new car
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_len=3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-280, 280)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def add_speed(self):
        self.car_speed += MOVE_INCREMENT





