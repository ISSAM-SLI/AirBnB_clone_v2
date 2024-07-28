#!/usr/bin/python3
"""
Initializes a Flask web application with multiple routes.
"""

from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    """ display number followed by  integers """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_n(n=None):
    """display a HTML page only if n is an intege"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def evn_odd(n=None):
    """display a HTML page only with an integer even or odd"""
    if (n % 2) == 0:
        result = "even"
    else:
        result = "odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
