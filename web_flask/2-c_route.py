#!/usr/bin/python3
'''Script that starts a Flask web application'''

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    '''Index route'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''/hbnb route'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def print_c_text(text):
    '''/c/<text> route'''
    text = text.replace("_", " ")
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
