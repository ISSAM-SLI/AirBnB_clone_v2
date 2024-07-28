#!/usr/bin/python3
"""
starts a Flask web application on 0.0.0.0:5000
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states():
    ''' renders a template page showing states listed by name '''
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    """Closes the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port='5000')
