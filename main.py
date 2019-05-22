import sys
import pygame
from time import sleep

import ioresolv
from settings import Settings
from dino import Dino
from cactus import Cactus
from button import Button


def run_game():

    crrnt_sttngs = Settings()
    # Screen vars
    screen_width = crrnt_sttngs.screen_width
    screen_height = crrnt_sttngs.screen_height
    bg_color = crrnt_sttngs.bg_color
    # Game vars
    init_speed = crrnt_sttngs.init_speed
    # Misc vars
    logo = pygame.image.load("assets/dino_still_ground.png")

    # Initialize the game and create a screen object
    pygame.init()
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Python Port of chrome://dino")
    screen = pygame.display.set_mode([screen_width, screen_height])

    # Init dino and cactus
    start_bt = Button(crrnt_sttngs, screen, "Play!")
    dino = Dino(screen, crrnt_sttngs)
    cactus = Cactus(screen, crrnt_sttngs, 'small')

    # Main loop of the game
    print("[INFO] The game starts.")
    
    #cactuses = Group()
    
    
    while True:

        # Use the ioresolv module to check events
        ioresolv.check_events(dino)
        dino.update(crrnt_sttngs.dhmax)
        sleep(1/crrnt_sttngs.init_speed)
        cactus.update()
        start_bt.update()

run_game()