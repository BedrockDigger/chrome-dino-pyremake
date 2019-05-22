import sys
from time import sleep

import pygame

from settings import Settings
import cactus


def check_events(dino):

        # Response to sys.exit() event and keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                dino.jumping = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
                dino.jumping = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
               dino.dodging = True
            elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
               dino.dodging = False

def alt_img(dino, propstr):
    if dino.altimg_counter == dino.settings.alt_freq:
        dino.image = pygame.image.load('assets/dino_' + propstr +
                                       '_' + str(dino.counter) + '.png')
        dino.altimg_counter = 0
        dino.counter = dino.counter * -1

def refresh_rect(rect):
    rect.screen.blit(rect.image, rect.rect)
    pygame.display.flip()

def refresh_screen(screen):
    screen.fill((255, 255, 255))

def dino_cord_reinit(dino):
    dino.rect.centery = dino.screen_rect.centery
    dino.rect.centerx = dino.screen_rect.left + 100

def cactus_cord_reinit(cactus):
    cactus.rect.x = cactus.rect.x - 10
    cactus.rect.centery = cactus.screen_rect.centery

def gravity(dino):
    if dino.crrnt_dh == -dino.settings.dhmax + 2:
        dino.crrnt_dh = dino.settings.dhmax
        print("[INFO] The dino jumped!")
    dino.crrnt_dh = dino.crrnt_dh - 2
    dino.rect.y = dino.rect.y - dino.crrnt_dh
    refresh_rect(dino)
    refresh_screen(dino.screen)

def spawn(screen, settings, cactuses):
    for cactusnum in range(10):
        cactus = cactus.SmallCactus(screen, settings)
        cactuses.add(cactus)