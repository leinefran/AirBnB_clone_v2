#!/usr/bin/python3
''' Flask Module'''


from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    ''' return welcoming str '''
    return 'Hello, HBNB!'


@app.route('/hbnb')
def display_HBNB():
    ''' returns HBNB '''
    return 'HBNB'


@app.route('/c/<text>')
def display_C(text=None):
    ''' return C and the value of the variable text '''
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    ''' return Python and the value of the variable text '''
    return 'Python {}'.format(text).replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
