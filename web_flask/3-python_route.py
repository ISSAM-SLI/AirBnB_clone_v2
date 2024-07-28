#!/usr/bin/python3
"""
Initializes a Flask web application with multiple routes.
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_page():
    """Returns a welcome message at the home route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_view():
    """Displays HBNB at the /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """Displays C followed by the value of text"""
    text = text.replace("_", " ")
    return f'C {escape(text)}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text="is_cool"):
    """ display Python followed by the value of text """
    text = text.replace("_", " ")
    return 'Python {}'.format(escape(text))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
