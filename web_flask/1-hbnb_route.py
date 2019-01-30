#!/usr/bin/python3
''' Flask Module'''


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' return welcoming str '''
    return 'Hello, HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display():
    ''' returns HBNB '''
    return 'HBNB'


if __name__ == '__main__':

    app.env = 'development'
    app.run(host='0.0.0.0', port=5000)
