#!/usr/bin/env python3
""" Module for basic flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ GET request to / """
    return render_template('0-index.html')
