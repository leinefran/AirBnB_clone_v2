#!/usr/bin/python3
''' Flask Module'''


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    ''' return welcoming str '''
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_HBNB():
    ''' returns HBNB '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_C(text=None):
    ''' return C and the value of the variable text '''
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    ''' return Python and the value of the variable text '''
    return 'C {}'.format(text).replace('_', ' ')


if __name__ == '__main__':

    app.env = 'development'
    app.run(host='0.0.0.0', port=5000)
