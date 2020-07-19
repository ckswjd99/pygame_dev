import pygame

#-- PYGAME INITIALIZE ------------------------------------------------------------------------------#
pygame.init()

#-- CONSTANTS ------------------------------------------------------------------------------#
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

#-- WINDOW SETTING ------------------------------------------------------------------------------#
size   = [1000, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Hello Game")

#-- CAMERA SETTING ------------------------------------------------------------------------------#
class camera:
    def __init__(self, focus):
        self.offset = [0,0]
        self.x_limit = [0,0]
        self.y_limit = [0,0]
        self.focus = focus
    def replace(self, x, y):
        self.offset[0] = x
        self.offset[1] = y

        #if self.x_limit[0] < x and x < self.x_limit[1]:
        #    self.offset[0] = x
        #if self.y_limit[0] < y and y < self.y_limit[1]:
        #    self.offset[1] = y
    def move(self, x, y):
        self.offset[0] += x
        self.offset[1] += y
        #if self.x_limit[0] < self.offset[0]+x and self.offset[0]+x < self.x_limit[1]:
        #    self.offset[0] += x
        #elif self.x_limit[0] > self.offset[0]+x:
        #    self.offset[0] = self.x_limit[0]
        #elif self.x_limit[1] < self.offset[0]+x:
        #    self.offset[0] = self.x_limit[1]

        #if self.y_limit[0] < self.offset[1]+y and self.offset[1]+y < self.y_limit[1]:
        #    self.offset[1] += y
        #elif self.y_limit[0] > self.offset[1]+y:
        #    self.offset[1] = self.y_limit[0]
        #elif self.y_limit[1] < self.offset[1]+y:
        #    self.offset[1] = self.y_limit[1]

    def set_x_limit(self, x1, x2):
        self.x_limit[0] = x1
        self.x_limit[1] = x2
    def set_y_limit(self, y1, y2):
        self.y_limit[0] = y1
        self.y_limit[1] = y2

    def set_focus(self, focus):
        self.focus = focus

    def update(self):
        # FOCUS ON FOCUS
        focus_smoothe = 5
        self.move(-(self.offset[0]+self.focus.pos[0]-size[0]/2)/focus_smoothe, -(self.offset[1]+self.focus.pos[1]-size[1]/2)/focus_smoothe )
        # LIMITS
        limit_smoothe = 3
        if self.offset[0] < self.x_limit[0]:
            self.move( (self.x_limit[0]-self.offset[0])/limit_smoothe, 0 )
        if self.offset[0] > self.x_limit[1]:
            self.move( (self.x_limit[1]-self.offset[0])/limit_smoothe, 0 )
        if self.offset[1] < self.y_limit[0]:
            self.move( 0, (self.y_limit[0]-self.offset[1])/limit_smoothe )
        if self.offset[1] > self.y_limit[1]:
            self.move( 0, (self.y_limit[1]-self.offset[1])/limit_smoothe )
