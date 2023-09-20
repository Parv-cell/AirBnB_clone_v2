#!/usr/bin/python3
""" Script that starts a Flask web application """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Returns the message to be displayed """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns the message to be displayed """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """ Returns the message to be displayed """
    processed_text = text.replace("_", " ")
    return f"C {processed_text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text="is cool"):
    """ Returns the message to be displayed """
    processed_text = text.replace("_", " ")
    return f"Python {processed_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Returns the message to be displayed """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Displays the HTML page """
    return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """ Dislays the HTML page containing even or odd number """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
