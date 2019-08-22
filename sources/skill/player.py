import multiprocessing 
import time
from pprint import pprint

processCurrent = None

def play(tempoName): 
  while True:
    print("Playing {}...".format(tempoName))
    time.sleep(2)


def player(tempoName):
  print("Player {}".format(tempoName))
  global processCurrent
  if (processCurrent is not None):
    print("Arrêt de {}".format(processCurrent.name))
    processCurrent.terminate()
    processCurrent.join(0.1)

  if ( tempoName != "end"):
    processCurrent = multiprocessing.Process(target=play, name=tempoName, args=(tempoName,)) 
    processCurrent.start()

