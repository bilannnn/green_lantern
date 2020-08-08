from flask import Blueprint

module1 = Blueprint('module1', __name__)


@module1.route("/")
def get_method():
    return "Hello from module 1"