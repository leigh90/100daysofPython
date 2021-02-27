from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.dot(20, 'white')
        self.shape('circle')
        self.color('white')
        self.penup()

    def moveright(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
