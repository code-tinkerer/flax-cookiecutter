from flask import Flask

from .{{cookiecutter.main_blueprint}} import {{cookiecutter.main_blueprint}}
from .dashboard import dashboard_app


def initialize(app: Flask):
    app.register_blueprint(dashboard_app, url_prefix="/dashboard")

    app.register_blueprint({{cookiecutter.main_blueprint}})
