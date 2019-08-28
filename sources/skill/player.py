# -*- coding: utf-8 -*-

from flask import Flask, Blueprint
from flask import request, g, current_app
import pygame
import time
import os

main = Blueprint('main', __name__, url_prefix="/alexa/player")
#Initialisation Pygame
pygame.mixer.init()

@main.route('/')
def player():
  return 'Player à votre écoute\n'

@main.route('/play/<mediafile>')
def play(mediafile):
  if "son" in  current_app.config:
    current_app.config["son"].stop()
  filePath = os.path.join(main.root_path, 'media', mediafile)
  son = pygame.mixer.Sound(filePath)
  son.play(-1)
  current_app.config["son"] = son
  return 'Media: play {}\n'.format(mediafile)

@main.route('/stop')
def stop():
  if "son" in  current_app.config:
    current_app.config["son"].stop()
  return 'Media: stop\n'

if __name__ == '__main__':
  # global app
  app = Flask(__name__)
  app.register_blueprint(main)
  app.run()
