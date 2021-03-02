from turtle import Turtle
FONT = ('Roboto', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(-150, 250)
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Level {self.score}', align='center', font=FONT )

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)

