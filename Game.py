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
        self.player = Player()
        self.all_sprites.add(self.player)
        platform1 = Platform(0, HEIGHT - 20, WIDTH, 20)
        self.all_sprites.add(platform1)
        self.platforms.add(platform1)
        platform2 = Platform(WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20)
        self.all_sprites.add(platform2)
        self.platforms.add(platform2)
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
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            self.player.position.y = hits[0].rect.top + 1
            self.player.velocity.y = 0
    
    def event(self):
        # game loop - events
        for event in pg.event.get():
            # check for closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

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