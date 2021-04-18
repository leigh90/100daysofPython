from flask import Flask

app = Flask(__name__)
# print(__name__)
print(type(__name__))

# >>> returns __main__

@app.route('/')
def hello_world():
    return 'Hello World'

# todo is a special atti__name__ the name of the class,function method, descriptor or generator instance

if __name__ == '__main__':
    app.run()


# Kernel is the actual system that interfaces with your hardware
# CLI 
