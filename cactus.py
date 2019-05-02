import random
import time
import pygame
from settings import Settings
from dino import Dino


class Cactus_Small():

    def __init__(self, dino_settings, screen):

        self.screen = screen
        self.dino_settings = dino_settings

        self.current_name = random.choice(range(4))
        self.image = pygame.image.load('elements/cactus_small_' +
                                       str(self.current_name) + '.png')
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)

    def update(self, dino_settings, dino_x, dino_y):

        self.dino_settings = Settings()

        if self.rect.x < dino_x:
            self.rect.x += dino_settings.cactus_speed_factor
        if self.rect.x > dino_x:
            self.rect.x -= dino_settings.cactus_speed_factor
        if self.rect.y < dino_y:
            self.rect.y += dino_settings.cactus_speed_factor
        if self.rect.y > dino_y:
            self.rect.y -= dino_settings.cactus_speed_factor
        time.sleep(0.01)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
