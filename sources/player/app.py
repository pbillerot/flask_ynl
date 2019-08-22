from flask import Flask, Blueprint
from flask import request

main = Blueprint('main', __name__, url_prefix="/player")

@main.route('/')
def player():
    return 'Liste des médias'

@main.route('/play')
def play():
    return 'Liste des médias'
