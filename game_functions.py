import sys
import pygame


def check_events(dino):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                dino.moving_right = True
            if event.key == pygame.K_LEFT:
                dino.moving_left = True
            if event.key == pygame.K_UP:
                dino.moving_up = True
            if event.key == pygame.K_DOWN:
                dino.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                dino.moving_right = False
            if event.key == pygame.K_LEFT:
                dino.moving_left = False
            if event.key == pygame.K_UP:
                dino.moving_up = False
            if event.key == pygame.K_DOWN:
                dino.moving_down = False

def update_screen(dino_settings, screen, dino, cactus):
    screen.fill(dino_settings.bg_color)
    dino.blitme()
    cactus.blitme()

#pygame.display.flip()
