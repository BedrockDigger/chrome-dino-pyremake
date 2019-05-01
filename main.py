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
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Python Port of chrome://dino")

    dino = Dino(ai_settings, screen)
    cactus = Cactus_Small(ai_settings, screen)

    while True:
        gf.check_events(dino)
        dino.update()
        #cactus.update()
        gf.update_screen(ai_settings, screen, dino, cactus)
        screen.fill(ai_settings.bg_color)
        dino.blitme()
        cactus.blitme()

        pygame.display.flip()

run_game()
