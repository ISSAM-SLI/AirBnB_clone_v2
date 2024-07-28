#!/usr/bin/python3
"""
Initializes a Flask web application with multiple routes.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Returns a greeting message at the home route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """Displays 'HBNB' at the /hbnb route."""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
