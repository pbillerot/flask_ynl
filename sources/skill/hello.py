from flask import Flask, Blueprint

main = Blueprint('main', __name__, url_prefix="/alexa")

@main.route('/')
def hello_world():
  print('Hello')
  return 'Hello, World!'

if __name__ == '__main__':
  app = Flask(__name__)
  app.register_blueprint(main)
  app.run()
