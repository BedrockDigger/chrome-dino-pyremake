import pygame.font

import ioresolv


class Button():

    def __init__(self, settings, screen, message):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200, 50
        self.bg_color = (83, 83, 83)
        self.txt_color = (218, 218, 218)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.mkmessage(message)

    def mkmessage(self, message):
        self.message_image = self.font.render(message, True, self.txt_color, self.bg_color)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)

    def update(self):
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)