import sys
from multiprocessing import Process
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
    screen = pygame.display.set_mode(    # init screen dimensions
        (dino_settings.screen_width, dino_settings.screen_height))
    pygame.display.set_caption("Python Port of chrome://dino")

    dino = Dino(dino_settings, screen)    # instancize the dino
    cactus = Cactus_Small(dino_settings, screen)

    def comp_main():
        while True:
            gf.update_screen(dino_settings, screen, dino, cactus)
            screen.fill(dino_settings.bg_color)
            dino.blitme()
            cactus.blitme()
            pygame.display.flip()

    def comp_dino():
        while True:
            gf.check_events(dino)
            dino.update(dino_settings)    # do dino actions while

    def comp_cactus():
        while True:
            cactus.update(dino_settings, dino.rect.x, dino.rect.y)

    if __name__ == '__main__':
        p1 = Process(target=comp_main)
        p1.start()
        p2 = Process(target=comp_dino)
        p2.start()
        p3 = Process(target=comp_cactus)
        p3.start()
        p1.join()
        p2.join()
        p3.join()

run_game()
