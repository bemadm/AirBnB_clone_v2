#!/usr/bin/python3
""" A script that starts a simple Flask web app.
    The app listens on 0.0.0.0, port 5000.
    Routes:
        /: Displays 'Hello HBNB!'
        /hbnb: Displays 'HBNB'
        /c/<text>: Displays 'C <text>'
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello(strict_slashes=False):
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hello_hbnb(strict_slashes=False):
    """Displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def hello_text(text, strict_slashes=False):
    """ Displays 'C ' followed by <text>"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
