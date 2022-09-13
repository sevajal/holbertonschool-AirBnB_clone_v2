#!/usr/bin/python3
'''Script that starts a Flask web application'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    '''Remove the current SQLAlchemy Session'''
    storage.close()


@app.route("/states_list", strict_slashes=False)
def display_states():
    '''Display a HTML page with the states'''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
