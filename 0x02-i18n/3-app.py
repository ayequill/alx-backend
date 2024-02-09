#!/usr/bin/env python3
""" Module for basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel, _
from babel_config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Select a language translation to use """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ GET request to / """
    return render_template('3-index.html',
                           title=_('home_title'), header=_('home_header'))