import eel
import os
from engine.command import *
from engine.features import *


def start():
    eel.init('www')

    playAssisteantSound()

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start("index.html", mode=None, host='localhost', block=True)
