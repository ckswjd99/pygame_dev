import pygame, numpy, poly
from setting import *

tile_size = 25

ground_whole = []

#---------- PRIMITIVE CLASS: BLOCK ----------#
class block:
    def __init__(self, pos_tile):
        self.pos_tile = pos_tile
        self.x = pos_tile[0]*tile_size
        self.y = pos_tile[1]*tile_size
        self.width = tile_size
        self.height = tile_size


#---------- CHILDREN CLASS: GROUND ----------#
class ground(block):
    def __init__(self, pos_tile):
        block.__init__(self, pos_tile)
        self.poly = pygame.Rect(self.x, self.y, self.width, self.height)
        ground_whole.append(self)
    
    def update(self):
        pass

    def render(self):
        pygame.gfxdraw.rectangle(screen, self.poly, RED)
        #hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.gfxdraw.rectangle(screen, hitbox, RED)



#---------- UTIL FUNCTION: BOARD ----------#
def board(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "g":
                ground((j,i))





#----------- TEST BENCH -----------#
if __name__ == "__main__":
    ground((1,1))
    ground((2,1))
    ground((3,1))
    print(ground_whole[0].poly)

    for g in ground_whole:
        g.render()
    
    pygame.display.flip()