#!/usr/bin/env python3
""" Module for basic flask app """
from flask import Flask, render_template
from flask_babel import Babel
from babel_config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', )
def index():
    """ GET request to / """
    return render_template('1-index.html')
