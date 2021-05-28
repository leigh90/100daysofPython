from flask import Flask
app = Flask(__name__)

def makebold(function):
    def wrapper_func():
        function()
        


@app.route('/')
def hello_world():
    return ""\
        "<h2>Hey you<h2>"\
        "<img src='https://media.giphy.com/media/wG9FYfl7SfsjK/giphy.gif'>"

@app.route("/bye")
def bye():
    return "Bye!"

@app.route('/username/<name>/')
def greet(name):
    return f"Hello {name} nice to have "

@app.route('/username/<name>/<int:post_id>')
def greeter(post_id,name):
    return f"Hello {name} nice to have {post_id}"

if __name__ == "__main__":
    app.run(debug=True)
    