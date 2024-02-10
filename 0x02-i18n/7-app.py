#!/usr/bin/env python3
""" Module for basic flask app """
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel
from babel_config import Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """ Select a language translation to use """
    lang = request.args.get('locale')
    print(lang)
    if lang and lang in app.config['LANGUAGES']:
        return lang
    if g.user:
        lang = g.user.get('locale')
        if lang and lang in app.config['LANGUAGES']:
            return lang
    lang = request.accept_languages.best_match(app.config['LANGUAGES'])
    if lang:
        return lang
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """determines the timezone to be used"""
    time_zone = request.args.get("timezone")
    if time_zone:
        try:
            pytz.timezone(time_zone)
            return time_zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user and g.user.get("timezone"):
        return g.user.get("timezone")
    return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route('/')
def index() -> str:
    """ GET request to / """
    return render_template('7-index.html',
                           user=g.user)


def get_user(login_as: int) -> dict:
    """ Returns a user dictionary """
    return users.get(login_as, None)


@app.before_request
def before_request() -> None:
    """ Invoked before a request """
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
    g.user = get_user(user_id)


if __name__ == "__main__":
    app.run(debug=True)
