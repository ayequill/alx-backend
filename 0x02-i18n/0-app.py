#!/usr/bin/env python3
""" Module for basic flask app """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> str:
    """ GET request to / """
    return render_template('0-index.html')
