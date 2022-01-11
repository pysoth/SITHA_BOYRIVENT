from pygame.math import Vector2
from creep import Creep
from avatar import avatar
from ennemis import ennemis
import core

import pygame

def setup():
    print("setup start....")
    core.fps = 30
    core.WINDOW_SIZE = [800,600]



def run () :
    core.cleanScreen()
    core.printMemory()


core.main (setup, run)