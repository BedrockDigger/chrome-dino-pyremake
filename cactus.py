import random
from time import sleep
import pygame

from settings import Settings
import ioresolv


class Cactus():

    def __init__(self, screen, settings, propstr):

        self.screen = screen
        self.settings = Settings()
        self.screen_rect = self.screen.get_rect()
        self.current_name = random.choice(range(1, 4))
        self.image = pygame.image.load('assets/cactus_' + propstr + '_' +
                                       str(self.current_name) + '.png')
        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.right
        self.rect.centery = self.screen_rect.centery
        ioresolv.refresh_rect(self)



    def update(self):
        ioresolv.cactus_cord_reinit(self)
        ioresolv.refresh_rect(self)


class SmallCactus(Cactus):

    def __init__(self, screen, settings):
        super().__init__(self, screen, settings, 'small')


class BigCactus(Cactus):

    def __init__(self, screen, settings):
        super().__init__(self, screen, settings, 'big')