import sys
import pygame
from settings import Settings
from dino import Dino
from cactus import Cactus_Small
import game_functions as gf


def run_game():
    pygame.init()
    logo = pygame.image.load("elements/custom_logo.png")
    pygame.display.set_icon(logo)
    dino_settings = Settings()
    screen = pygame.display.set_mode(
        (dino_settings.screen_width, dino_settings.screen_height))
    pygame.display.set_caption("Python Port of chrome://dino")

    dino = Dino(dino_settings, screen)
    cactus = Cactus_Small(dino_settings, screen)

    while True:
        gf.check_events(dino)
        dino.update(dino_settings)
        # cactus.update()
        gf.update_screen(dino_settings, screen, dino, cactus)
        screen.fill(dino_settings.bg_color)
        dino.blitme()
        cactus.blitme()

        pygame.display.flip()

run_game()
