from flask import Flask, Blueprint

main = Blueprint('main', __name__, url_prefix="/alexa")

@main.route('/')
def hello_world():
    return 'Hello, World!'

