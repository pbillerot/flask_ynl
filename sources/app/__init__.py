from flask import Flask

from .app import main

application = Flask(__name__)
application.register_blueprint(main)
