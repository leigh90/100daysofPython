import turtle

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#TODO
# 1. Read the CSV data
import pandas
data = pandas.read_csv('50_states.csv')
# print(states_data)
# print(type(states_data))

all_states = data.state.to_list()
guessed_states = []
# 2. Store the states and their coordinates into a usable type
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} Guess the state", prompt="Add another state").title()
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        print(missing_states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_tolearn.csv')
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
# 3. Get user input

# 4. Check user input
# 5. Write input to specific coordinate
# 6. Keep track of score in input
# 7.

screen.exitonclick()
