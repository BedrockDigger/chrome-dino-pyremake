import pygame
from settings import Settings


class Dino():

    def __init__(self, dino_settings, screen):

        self.screen = screen
        self.dino_settings = dino_settings

        self.image = pygame.image.load('elements/dino_still.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.x = self.screen_rect.x
        self.rect.y = self.screen_rect.y

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self, dino_settings):

        self.dino_settings = Settings()

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += 1*dino_settings.dino_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.x -= 1*dino_settings.dino_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= 1*dino_settings.dino_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += 1*dino_settings.dino_speed_factor

        if dino_settings.dino_debug is True:
            print("INFO Current dino cord: " +
                  str(self.rect.x) + ", " + str(self.rect.y))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
