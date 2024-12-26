from flask import (
    Blueprint,
    render_template,
)

{{cookiecutter.main_blueprint}} = Blueprint("{{cookiecutter.main_blueprint}}", __name__)


@{{cookiecutter.main_blueprint}}.get("/")
def index():
    return render_template("pages/{{cookiecutter.main_blueprint}}/index.html")
