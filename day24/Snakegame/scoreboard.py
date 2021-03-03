from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score:{self.high_score}' , align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')

        self.score = 0
        self.update_score()

    def update_highscore(self):
        if self.score > self.high_score:
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')



