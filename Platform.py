# sprite classes for platformer game
import pygame as pg
from settings import *
vector = pg.math.Vector2


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width, heigth):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, heigth))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
