#!/usr/bin/env python3
""" flask app """
from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """ Config class """
    LANGUAGES = ['en', 'fr']
    DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def index() -> str:
    """ index page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
