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

# CAMERA SETTING
class camera:
    def __init__(self):
        self.offset = [0,0]
        self.x_limit = [0,0]
        self.y_limit = [0,0]
    def replace(self, x, y):
        if self.x_limit[0] < x and x < self.x_limit[1]:
            self.offset[0] = x
        if self.y_limit[0] < y and y < self.y_limit[1]:
            self.offset[1] = y
    def move(self, x, y):
        if self.x_limit[0] < self.offset[0]+x and self.offset[0]+x < self.x_limit[1]:
            self.offset[0] += x
        if self.y_limit[0] < self.offset[1]+y and self.offset[1]+y < self.y_limit[1]:
            self.offset[1] += y
    def set_x_limit(self, x1, x2):
        self.x_limit[0] = x1
        self.x_limit[1] = x2
    def set_y_limit(self, y1, y2):
        self.y_limit[0] = y1
        self.y_limit[1] = y2

cam = camera()

#-- GENERATE PLAYER ------------------------------------------------------------------------------#
import character as ch
player_bstat = ch.basic_stat(acc=3, jump_power=10, max_speed=10, max_hp=100, max_mp=100)
player_phstat = ch.physics_stat(width=20, height=20, air_drag=0.2)
player = ch.player("1P", (500,400), player_bstat, player_phstat)
