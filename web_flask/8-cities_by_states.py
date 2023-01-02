#!/usr/bin/python3
""" A script that starts a simple Flask web app.
    The app listens on 0.0.0.0, port 5000.
    Routes:
        /cities_by_states: displays the list of cities
            on an html paage, according to their states
"""
from flask import Flask
from flask import render_template
from models import storage


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """ Displays and HTML page with a list of all
        objects stored in the Storage (DBStorage or FileStorage)
        where the resulting state list is sorted by name.
    """
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Method to remove current SQLAlchemy session
       after each request
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
