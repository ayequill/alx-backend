#!/usr/bin/env python3
""" Module for basic flask app """
from flask import Flask, render_template, request
from flask_babel import Babel
from babel_config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Select a language translation to use """
    lang = request.args.get('locale')
    if lang and lang in app.config['LANGUAGES']:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ GET request to / """
    return render_template('4-index.html')
