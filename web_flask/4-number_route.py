#!/usr/bin/python3
""" A script that starts a simple Flask web app.
    The app listens on 0.0.0.0, port 5000.
    Routes:
        /: Displays 'Hello HBNB!'
        /hbnb: Displays 'HBNB'
        /c/<text>: Displays 'C <text>'
        /python/(<text>): Displays 'Python <text>'
        /number/<n>: display 'n is a number' if n is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text():
    """ Displays 'C ' followed by <text>"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """ Displays 'Python ' followed by <text>"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_int(n):
    """ Displays 'n is a number' only if n is an integer"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
