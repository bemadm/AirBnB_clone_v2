#!/usr/bin/python3
""" A script that starts a simple Flask web app.
    The app listens on 0.0.0.0, port 5000.
    Routes:
        /states_list: displays the list of states
            on an html paage
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Method to remove current SQLAlchemy session
       after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
