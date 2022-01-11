from pygame.math import Vector2
import pygame
import random
import core


class avatar(Drawable):
    """Used to represent the concept of a player.
    """
    COLOR_LIST = [
        (37, 7, 255),
        (35, 183, 253),
        (48, 254, 241),
        (19, 79, 251),
        (255, 7, 230),
        (255, 7, 23),
        (6, 254, 13)]

    FONT_COLOR = (50, 50, 50)

    def __init__(self, surface, camera, name=""):
        super().__init__(surface, camera)
        self.x = random.randint(100, 400)
        self.y = random.randint(100, 400)
        self.mass = 20
        self.speed = 4
        self.color = col = random.choice(avatar.COLOR_LIST)
        self.outlineColor = (
            int(col[0] - col[0] / 3),
            int(col[1] - col[1] / 3),
            int(col[2] - col[2] / 3))
        if name:
            self.name = name
        else:
            self.name = "Anonymous"
        self.pieces = []
