import pygame, numpy, poly

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



from setting import *
#---------- CHILDREN CLASS: WALL ----------#
class wall(block):
    def __init__(self, parent_map, pos_tile):
        block.__init__(self, parent_map, pos_tile)
        self.image = pygame.image.load("img/block/wall.png")
        wall_whole.append(self)

        self.collision_character = True
        self.collision_ray = True
    
    def update(self):
        pass

    def render(self):
        #pygame.gfxdraw.rectangle(screen, self.poly, RED)
        screen.blit(self.image, (self.x + camera_offset[0], self.y + camera_offset[1]))
        #hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        #pygame.gfxdraw.rectangle(screen, hitbox, RED)



#---------- CHILDREN CLASS: INVISIBLE WALL ----------#
class invisible_wall(block):
    def __init__(self, parent_map, pos_tile):
        block.__init__(self, parent_map, pos_tile)
        self.image = pygame.image.load("img/block/wall.png")
        wall_whole.append(self)

        self.collision_character = True
        self.collision_ray = True
    
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
            screen.blit(self.image_inactive, (self.x + camera_offset[0], self.y + camera_offset[1]))
        else:
            screen.blit(self.image_active, (self.x + camera_offset[0], self.y + camera_offset[1]))

        


        


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
