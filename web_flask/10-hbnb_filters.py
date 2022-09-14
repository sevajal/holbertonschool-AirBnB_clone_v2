#!/usr/bin/python3
'''Script that starts a Flask web application'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    '''Remove the current SQLAlchemy Session'''
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def display_filters():
    '''Display a HTML page with filters'''
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('6-index.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
