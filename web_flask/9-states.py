#!/usr/bin/python3
'''Script that starts a Flask web application'''

from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    '''Remove the current SQLAlchemy Session'''
    storage.close()


@app.route("/states", strict_slashes=False)
def display_states():
    '''Display a HTML page with the states'''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def display_cities_of_a_state(id):
    '''Display a HTML page with the states'''
    states = storage.all(State).values()
    state_name = ""
    for state in states:
        if state.id == id:
            state_name = state.name
    return render_template(
        '9-states.html', id=id, states=states, state_name=state_name)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
