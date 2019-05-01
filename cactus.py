import random
import time
import pygame
from settings import Settings


class Cactus_Small():

    def __init__(self, ai_settings, screen):

        self.screen = screen
        self.ai_settings = ai_settings

        self.current_name = random.choice(range(4))
        self.image = pygame.image.load('elements/cactus_small_' \
         + str(self.current_name) + '.png')
        self.rect = self.image.get_rect()

#        self.rect.centerx = dino.screen_rect.centerx
#        self.rect.bottom = dino.screen_rect.bottom

        self.x = float(self.rect.x)

    #def update(self):
#        self.rect.centerx = dino.screen_rect.centerx
    #    self.rect.bottom = dino.screen_rect.bottom
    #    time.sleep(0.5)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
