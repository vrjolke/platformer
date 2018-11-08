# sprite classes for platformer game
import pygame as pg
from settings import *
vector = pg.math.Vector2


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 40))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.position = vector(WIDTH / 2, HEIGHT / 2)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, 0)

    def update(self):
        self.acceleration = vector(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acceleration.x = -PLAYER_ACCELERATION
        if keys[pg.K_RIGHT]:
            self.acceleration.x = PLAYER_ACCELERATION

        self.acceleration.x += self.velocity.x * PLAYER_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5 * self.acceleration
        # wrap around the sides of the screen
        if self.position.x > WIDTH:
            self.position.x = 0
        if self.position.x < 0:
            self.position.x = WIDTH

        self.rect.midbottom = self.position

    def jump(self):
        self.rect.x += 1
        collision = pg.sprite.spritecollide(self, self.game.platforms, False) 
        self.rect.x -= 1
        if collision:
            self.velocity.y = -20
