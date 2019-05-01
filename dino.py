import pygame
from settings import Settings


class Dino():

    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('elements/dino_still.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.dino_debug = False     # Switch to trigger debug output in stdout

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.bottom -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1
        if self.dino_debug == True:
            print("INFO Current dino cord: " + str(self.rect.centerx) + ", " + str(self.rect.bottom))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
