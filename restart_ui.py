import pygame


class restart_ui(self):

    self.screen = screen
    self.screen_rect = screen.get_rect()

# TODO: refresh highscore board

    self.width, self.height = 200, 50
    self.button_color = (83, 83, 83)
    self.text.color = (225, 225, 225)
    self.font = pygame.font.Sysfont(None, 48)

    self.rect = pygame.rect(0, 0, self.width, self.height)
    self.rect.center = self.screen_rect.center
