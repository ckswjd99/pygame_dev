import pygame

#-- 1. initialize pygame --#
pygame.init()

# 2. 기본 환경 세팅
## Frames per Second
FPS = 30
## COLORS FOR USE
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED   = (255,   0,   0)

YELLOW= (255, 212,   0)
ORANGE= (255, 127,   0)

# WINDOW SETTING
size   = [1000, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hello Game")

camera_offset = [20,20]

#-- GENERATE PLAYER ------------------------------------------------------------------------------#
import character as ch
player_bstat = ch.basic_stat(acc=3, jump_power=10, max_speed=10, hp=100)
player_phstat = ch.physics_stat(width=20, height=20, air_drag=0.2)
player = ch.player("1P", (500,400), player_bstat, player_phstat)
