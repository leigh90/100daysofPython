from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/bye')
def bye():
    return 'Bye'

@app.route("/username/<name>")
def greet(name):
    return f"Hello, welcome back {name} "

@app.route("/username/<name>/<int:number>")
def converter(name, number):
    return " <h1>Hello, welcome back {name} and you are {number} years old<h1>"\
            "<img src='https://media.giphy.com/media/iavKpDrWkA8Io/giphy.gif'>"


if __name__ == '__main__':
    app.run(debug=True)