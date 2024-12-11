from flask import Flask

from .{{cookiecutter.main_blueprint}} import {{cookiecutter.main_blueprint}}


def initialize(app: Flask):
    app.register_blueprint({{cookiecutter.main_blueprint}})
