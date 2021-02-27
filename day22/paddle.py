from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setposition(position)
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        # self.goto(350, 0)
        # self.setposition(350, 0)

    def paddleup(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddledown(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


