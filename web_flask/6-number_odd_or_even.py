#!/usr/bin/python3
""" A script that starts a simplr Flask web app.
    It listens on 0.0.0.0, port 5000.
    Routes:
        /: Displays 'Hello HBNB!'
        /hbnb: Displays 'HBNB'
        /c/<text>: Displays 'C <text>'
        /python/(<text>): Displays 'Python <text>'
        /number/<n>: Displays 'n is a number' if n is an integer
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/', strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text():
    """Displays 'C' followed by <text>"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """Displays 'Python ' followed by <text>"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_int(n):
    """Displays 'n is a number' only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_number_int(n):
    """Displays an html page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def html_number_div(n):
    """Displays an html page only if n is an integer"""
    if (n % 2 == 0):
        type = 'even'
    else:
        type = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, type=type)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
