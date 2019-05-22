from time import sleep
import pygame

import ioresolv
from settings import Settings


class Dino():

    def __init__(self, screen, settings):

        self.image = pygame.image.load('assets/dino_still.png')
        self.screen = screen
        self.settings = Settings()
        self.screen_rect = self.screen.get_rect()
        self.rect = self.image.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.left + 100
        ioresolv.refresh_rect(self)

        self.jumping = False
        self.dodging = False
        self.counter = 1
        self.altimg_counter = 0
        self.crrnt_dh = self.settings.dhmax


    def update(self, dhmax):

        if self.jumping or self.rect.centery != self.screen_rect.centery:
           self.image = pygame.image.load('assets/dino_still.png')
           ioresolv.gravity(self)

        elif self.dodging:
            ioresolv.alt_img(self, 'dodging')
            print("[INFO] The dino dodges!")
            self.rect = self.image.get_rect()
            ioresolv.dino_cord_reinit(self)
            ioresolv.refresh_rect(self)
            ioresolv.refresh_screen(self.screen)
            self.altimg_counter = self.altimg_counter + 1

        else:
            ioresolv.alt_img(self, 'running')
            self.rect = self.image.get_rect()
            ioresolv.dino_cord_reinit(self)
            ioresolv.refresh_rect(self)
            ioresolv.refresh_screen(self.screen)
            self.altimg_counter = self.altimg_counter + 1