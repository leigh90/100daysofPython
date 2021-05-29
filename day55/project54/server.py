from flask import Flask
app = Flask(__name__)
import random

@app.route('/')
def index():
    return """
    <h1>Guess a number between 0 and 9</h1>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">
    """

@app.route('/<int:num>')
def number(num):
    # import random number
    random_num = random.randint(0,10)
    print(random_num)
    if num == random_num:
        print('Gatchu')
        return f"I Gatchu <h1>Random number {random_num}, Your number is {num}</h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif num > random_num:
        print('Too High')
        return f"Too High, Your number {num} the random number is {random_num}"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    elif num < random_num:
        print('Sorry no dice')
        return f"Too low <h1>Random number {random_num}, Your number is {num} </h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"



if __name__ == "__main__":
    app.run(debug=True)