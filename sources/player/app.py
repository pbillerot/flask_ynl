from flask import Flask, Blueprint
from flask import request

import pygame
from pygame.locals import *

main = Blueprint('main', __name__, url_prefix="/player")
#Initialisation Pygame
pygame.mixer.init()
son = None

@main.route('/')
def player():
  return 'Liste des médias'

@main.route('/play/<mediafile>')
def play(mediafile):
  global son
  son = pygame.mixer.Sound("./media/drums_100.wav")
  son.play(-1)
  return 'Media: {}'.format(mediafile)

@main.route('/stop')
def stop():
  global son
  if son is not None:
    son.stop
  return 'Media: stop'

if __name__ == '__main__':
  app = Flask(__name__)
  app.register_blueprint(main)
  app.run()
