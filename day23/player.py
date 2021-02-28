from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setposition(0, -270)
        self.setheading(90)
        self.move_distance = MOVE_DISTANCE

    def move(self):
        self.forward(self.move_distance)


