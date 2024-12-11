from flask import Flask

from dotenv import load_dotenv
load_dotenv()

import jinja_partials

def create_app(config_name="development"):
    app = Flask(__name__, static_folder="../{{cookiecutter.static_folder}}")

    initialize_context(app)
    initialize_config(app, config_name)
    initialize_extensions(app)
    initialize_routes(app)

    return app


def initialize_context(app: Flask):
    @app.context_processor
    def inject_app_context():
        return { "app": app }


def initialize_config(app: Flask, config_name="development"):
    if config_name in ["development", "testing", "production"]:
        app.config.from_object(f"config.{config_name}")
    else:
        app.config.from_object("config.development")


def initialize_extensions(app: Flask):
    jinja_partials.register_extensions(app)


def initialize_routes(app: Flask):
    from app import routes

    routes.initialize(app)