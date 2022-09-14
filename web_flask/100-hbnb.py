#!/usr/bin/python3
'''Script that starts a Flask web application'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.teardown_appcontext
def close_session(self):
    '''Remove the current SQLAlchemy Session'''
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def display_airbnb():
    '''Display a HTML page with filters'''
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User).values()
    return render_template(
        '10-hbnb_filters.html', states=states, amenities=amenities, places=places, users=users)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
