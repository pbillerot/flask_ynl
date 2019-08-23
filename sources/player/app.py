# -*- coding: utf-8 -*-

from flask import Flask, Blueprint
from flask import request, g, current_app

import pygame

import time
import pprint

main = Blueprint('main', __name__, url_prefix="/player")
#Initialisation Pygame
pygame.mixer.init()

@main.route('/')
def player():
  return 'Liste des médias\n'

@main.route('/play/<mediafile>')
def play(mediafile):
  if "son" in  current_app.config:
    current_app.config["son"].stop()
  son = pygame.mixer.Sound("media/" + mediafile)
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
