#!/usr/bin/python3
"""Starts a Flask web application.
Application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closedb(exc):
    """ Close a database session"""
    storage.close()


@app.route('/cities_by_states')
def states_list():
    """ states_list route """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    storage.reload()
    app.run("0.0.0.0", 5000)
