from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

tim.speed(0.0010)
# # tim.forward(100)
# # tim.right(180)
# # tim.forward(100)
# tim.setheading(97)
# # tim.left(180)
# # tim.forward(100)
# # tim.tilt(97)
# tim.degrees(fullcircle=360.0)
# tim.forward(100)
# tim.circle(50, 360, 56)
# tim.settiltangle(30)
# tim.fd(50)
tim.forward(100)
tim.clear()





def move_forward():
    tim.forward(100)

def move_backward():
    tim.backward(100)

def turn
def counter_clockwise():
    tim.right(10)
    # tim.forward(100)
    pass

def anticlockwise():
    tim.left(10)
    pass

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()


screen.listen()
# onkey is a higherorder function that takes in a function and a eventlistenter and calls the function when the event is triggered.
# try to use positional arguments for easy readability and understandability
screen.onkey(key='space', fun=move_forward)
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=anticlockwise)
screen.onkey(key='c', fun=clear_drawing)


screen.exitonclick()

