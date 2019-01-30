#!/usr/bin/python3
''' Flask Module'''


from flask import Flask


web_app = Flask(__name__)


@web_app.route('/', strict_slashes=False)
def hello():
    ''' return welcoming str '''
    return 'Hello, HBNB!'

@web_app.route('/hbnb', strict_slashes=False)
def display():
    ''' returns HBNB '''
    return 'HBNB'


if __name__ == '__main__':

    web_app.env = 'development'
    web_app.run(host='0.0.0.0', port=5000)
