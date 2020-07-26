import pygame, numpy, poly
from setting import *

TILE_SIZE = 25

#---------- CONSTANTS ----------#
PLAYER_COLLIDE = 0
CHARACTER_COLLIDE = 1


wall_whole = []   # blocks that BLOCKS characters

#---------- PRIMITIVE CLASS: BLOCK ----------#
class block:
    def __init__(self, parent_map, pos_tile):
        self.map = parent_map
        self.pos_tile = pos_tile
        self.x = pos_tile[0]*TILE_SIZE
        self.y = pos_tile[1]*TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE
        self.poly = pygame.Rect(self.x, self.y, self.width, self.height)
        
        self.collision_character = False
        self.collision_ray = False




#---------- CHILDREN CLASS: WALL ----------#
class wall(block):
    def __init__(self, parent_map, pos_tile):
        block.__init__(self, parent_map, pos_tile)
        self.image = pygame.image.load("img/block/wall.png")
        wall_whole.append(self)

        self.collision_character = True
        self.collision_ray = True

    def set_image(self, image):
        self.image = image
    
    def update(self):
        pass

    def render(self):
        #pygame.gfxdraw.rectangle(screen, self.poly, RED)
        screen.blit(self.image, (self.x + self.map.cam.offset[0], self.y + self.map.cam.offset[1]))
        #hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.gfxdraw.rectangle(screen, hitbox, RED)



#---------- CHILDREN CLASS: INVISIBLE WALL ----------#
class invisible_wall(block):
    def __init__(self, parent_map, pos_tile):
        block.__init__(self, parent_map, pos_tile)
        self.image = pygame.image.load("img/block/wall.png")
        wall_whole.append(self)

        self.collision_character = True
        self.collision_ray = False
    
    def update(self):
        pass

    def render(self):
        pass


#---------- CHILDREN CLASS: EVENT BLOCK ----------#
class eventblock(block):
    def __init__(self, parent_map, pos_tile, condition, func):
        block.__init__(self, parent_map, pos_tile)
        self.image_inactive = pygame.image.load("img/block/eventblock_inactive.png")
        self.image_active = pygame.image.load("img/block/eventblock_active.png")
        self.condition = condition
        self.func = func
        self.active = False
        
        self.collision_character = False
        self.collision_ray = False
    
    def update(self):
        if self.active == False:
            if self.condition == PLAYER_COLLIDE:
                if self.poly.colliderect(self.map.player.poly):
                    self.func()
                    self.active = True
            elif self.condition == CHARACTER_COLLIDE:
                for ch in self.map.characters:
                    if self.poly.colliderect(ch.poly):
                        self.func()
                        self.active = True
        else:
            self.active = False
            if self.condition == PLAYER_COLLIDE:
                if self.poly.colliderect(self.map.player.poly):
                    self.active = True
            elif self.condition == CHARACTER_COLLIDE:
                for ch in self.map.characters:
                    if self.poly.colliderect(ch.poly):
                        self.active = True

    def render(self):
        if self.active == False:
            screen.blit(self.image_inactive, (self.x + self.map.cam.offset[0], self.y + self.map.cam.offset[1]))
        else:
            screen.blit(self.image_active, (self.x + self.map.cam.offset[0], self.y + self.map.cam.offset[1]))


#---------- CHILDREN CLASS: PORTAL BLOCK ----------#
class portalblock(block):
    def __init__(self, parent_map, pos_tile, to_map, to_pos):
        block.__init__(self, parent_map, pos_tile)
        self.to_map = to_map
        self.to_pos = to_pos
        self.image = pygame.image.load("img/block/portal.png")
        
        self.collision_character = False
        self.collision_ray = False

        self.active = False
    
    def update(self):
        if self.poly.colliderect(self.map.player.poly) and self.active == False:
            self.map.move_map(self.to_map, self.to_pos)
            self.active = True

    def render(self):
        screen.blit(self.image, (self.x + self.map.cam.offset[0], self.y + self.map.cam.offset[1]))
        
        


        


#---------- UTIL FUNCTION: BOARD ----------#
def board(parent_map, map_array):
    result = []
    for i in range(len(map_array)):
        for j in range(len(map_array[i])):
            if map_array[i][j] == "g":
                result.append( wall(parent_map, (j,i)) )
                
    return result


map_array_example = [
        ["g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g","g"]
    ]



#----------- TEST BENCH -----------#
if __name__ == "__main__":
    wall(False, (1,1))
    wall(False, (2,1))
    wall(False, (3,1))
    print(wall_whole[0].poly)

    for g in wall_whole:
        g.render()
    
    pygame.display.flip()
