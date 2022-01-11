from pygame.math import Vector2
import pygame
import random
import core


class creep(Drawable):  # Semantically, this is a parent class of player
    """Used to represent the fundamental entity of game.
    A cell can be considered as a quantom of mass.
    It can be eaten by other entities.
    """
    CELL_COLORS = [
        (80, 252, 54),
        (36, 244, 255),
        (243, 31, 46),
        (4, 39, 243),
        (254, 6, 178),
        (255, 211, 7),
        (216, 6, 254),
        (145, 255, 7),
        (7, 255, 182),
        (255, 6, 86),
        (147, 7, 255)]

    def __init__(self, surface, camera):
        super().__init__(surface, camera)
        self.x = random.randint(20, 1980)
        self.y = random.randint(20, 1980)
        self.mass = 7
        self.color = random.choice(creep.CELL_COLORS)

    def draw(self):
        """Draws a cell as a simple circle.
        """
        zoom = self.camera.zoom
        x, y = self.camera.x, self.camera.y
        center = (int(self.x * zoom + x), int(self.y * zoom + y))
        pygame.draw.circle(self.surface, self.color, center, int(self.mass * zoom))




