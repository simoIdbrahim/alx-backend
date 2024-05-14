#!/usr/bin/env python3
""" flask app """
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
from datetime import timezone as tmzn
from pytz import timezone
import pytz.exceptions
from typing import (
    Dict,
    Union
)


class Config(object):
    """ Config CLASS """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ get user method """
    id = request.args.get('login_as', None)
    if id and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """ """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """ """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    if g.user:
        loc = g.user.get('locale')
        if loc and loc in app.config['LANGUAGES']:
            return loc
    loc = request.headers.get('locale', None)
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ current time"""
    current_time = request.args.get('timezone', None)
    if current_time:
        try:
            return timezone(current_time).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            current_time = g.user.get('timezone')
            return timezone(current_time).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    default_t = app.config['BABEL_DEFAULT_TIMEZONE']
    return default_t


@app.route('/', strict_slashes=False)
def index() -> str:
    """ index page """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
