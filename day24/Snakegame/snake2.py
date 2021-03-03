from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.full_snake.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.full_snake[-1].position())

    def move(self):
        for snake_seg in range(len(self.full_snake)-1,0,-1):
            new_x = self.full_snake[snake_seg-1].xcor()
            new_y = self.full_snake[snake_seg-1].ycor()
            self.full_snake[snake_seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """
        Reset the game when the game ends either by player hitting wall or sellf
        """
        # remove the old snake from view by sending it off screen when the gam ends
        for segment in self.full_snake:
            segment.goto(1000, 1000)
        self.full_snake.clear()
        # recreate the snake again for a new game
        self.create_snake()
        # set the head of the snake
        self.head = self.full_snake[0]

    # go up
    # tim.setheading(90)
    # tim.forward(100)
    # # turn left
    # tim.setheading(180)
    # tim.forward(100)
    # go down
    # tim.setheading(270)
    # tim.forward(120)
    # # go right
    # tim.setheading(0)
    # tim.forward(100)


    from turtle import Screen, Turtle



    import time
    #
    # screen = Screen()
    # screen.setup(width=600, height=600)
    # screen.bgcolor("black")
    # screen.title('Snake Ninja')
    # screen.tracer(0)
    #
    # # STEP 1: SNAKE BODY
    # segments = []
    # positions = [(0, 0), (-20, 0), (-40, 0)]
    # for position in positions:
    #     new_segment = Turtle(shape='square')
    #     new_segment.color('white')
    #     new_segment.penup()
    #     new_segment.goto(position)
    #     segments.append(new_segment)
    #
    # print(len(segments))
    # # MOVE THE SNAKE
    # game_on = True
    # while game_on:
    #     screen.update()
    #     time.sleep(0.1)
    #     for seg_num in range(len(segments) - 1, 0, -1):
    #         new_x = segments[seg_num - 1].xcor()
    #         print(f'seg_num is {seg_num}')
    #         print(f' segments is {segments}')
    #         print(f'segments[seg_num] is {segments[seg_num]}')
    #         new_y = segments[seg_num - 1].ycor()
    #         segments[seg_num].goto(new_x, new_y)
    #     segments[0].forward(20)
    #     segments[0].left(90)
    #
    # screen.exitonclick()
