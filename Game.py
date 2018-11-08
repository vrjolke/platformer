import pygame as pg
import random
from settings import *
from Player import *
from Platform import *


class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()  # for sound effects
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()  # handles the speed
        self.running = True

    def new(self):
        # start new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        for platform in PLATFORM_LIST:
            platform_to_add = Platform(*platform)
            self.all_sprites.add(platform_to_add)
            self.platforms.add(platform_to_add)
        self.run()

    def run(self):
        # game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def update(self):
        # game loop - update
        self.all_sprites.update()
        # check collision only when falling downwards
        if self.player.velocity.y > 0:
            collision = pg.sprite.spritecollide(self.player, self.platforms, False)
            if collision:
                self.player.position.y = collision[0].rect.top + 1
                self.player.velocity.y = 0
                self.player.jump()
    
    def event(self):
        # game loop - events
        for event in pg.event.get():
            # check for closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            # jumping
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if self.player.velocity.y == 0:
                        self.player.jump()

    def draw(self):
        # game loop - draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):

        pass

    def show_gameover_screen(self):
        # game over / continue
        pass

game = Game()
game.show_start_screen()

while game.running:
    game.new()
    game.show_gameover_screen()

pg.quit()