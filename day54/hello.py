from flask import Flask
import requests

app = Flask(__name__)
print(__name__)
# __name__ = name of the file.
# >>> returns __main__
print(type(__name__))
print(requests.__name__)

# this decorator checks that the user has requested the  url with / and only triggers the hello world function
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/bye')
def say_bye():
    return 'Bye love'
#  is a special attiribute __name__ the name of the class,function method, descriptor or generator instance

# if __name__ == '__main__':
#     app.run()


# Kernel is the actual system that interfaces with your hardware
# CLI 

