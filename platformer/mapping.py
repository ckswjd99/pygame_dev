############################## README ############################################################
##  This file defines class 'mapping'. 
##  It was originally 'map' but changed to 'mapping' to avoid crash with Python basic function.
## 
##  mapping class manages core attributes for ovrall gameplay.
##  
##  mapping class contains following attributes:
##      > size_tiles            : defined & assigned in __init__.
##      > blocks                : defined in __init__, assigned in map_setting, add_block
##      > characters            : defined in __init__, assigned in map_setting.
##      > UI                    : defined & assigned in __init__.
##      > effect_screen         : defined & assigned in __init__. 
##      > image_background      : defined & assigned in background_setting.
##      > spawn_list            : defined & assigned in map_setting. list of preset spawn positions.
##      > game_runner           : defined & assigned in start. main loop manger.
##      > player                : defined & assigned in start. player object.
##      > cam                   : defined & assigned in start. cam object.
##  
##  and following functions:
##      > __init__(self, size_tiles)        : init function. only gets number of tiles in row, col.
##      > background_setting(self, image)   : set background image.
##      > map_setting(self, block_array, spawn_list, char_array)
##              : ESSENTIAL. sets attribute blocks, spawn_list, characters.
##      > add_block(self, *block)           : gets array of blocks, append to blocks.
##      > start(self, game_runner, player, pos)
##              : ESSENTIAL. pass game_runner, player and its position.
##      > update(self)                      : updates event, player, effect, camera, blocks, UI
##      > render(self)                      : renders background, block, effect, player, UI
##  
##  In order to make one map, you should run these functions:
##      > __init__, background_setting, map_setting
##  
##  And when you call runner.map_change, then mapping.start will called automatically.
##  
##################################################################################################

from setting import *
import pygame
import entity
import effect
import UI
import character
import attack
import camera
import numpy
import ray

from PIL import Image, ImageFilter

#---------- CONSTANTS ----------#
TRANSITION_NONE = 0
TRANSITION_OPEN = 1
TRANSITION_CLOSE = 2


# MAP EXAMPLE
map_temp = [
        ["g","g","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
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
        ["0","0","0","0","g","0","g","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","g"],
        ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","g","g"]
    ]

#---------- PRIMITIVE CLASS: MAP ----------#
class mapping:
    def __init__(self, size_tiles):
        self.size_tiles = size_tiles
        
        self.blocks = []
        for i in range(-1, size_tiles[0]+1):
            self.blocks.append( entity.invisible_wall(self, (i,-1)) )
            self.blocks.append( entity.invisible_wall(self, (i,size_tiles[1])) )
        for i in range(size_tiles[1]):
            self.blocks.append( entity.invisible_wall(self, (-1,i)) )
            self.blocks.append( entity.invisible_wall(self, (size_tiles[0],i)) )

        self.characters = []
        self.carpets = []

        self.UI = UI.UI(self)

        self.effect_screen = pygame.Surface(size)
        self.transition_delay = 20
        self.transition_tick = 0
        self.transition_type = TRANSITION_NONE

        self.darkness = 0.9
        self.lights = []

    def background_setting(self, image):
        self.image_background = image

    def move_map(self, to_map, to_pos):
        self.transition_type = TRANSITION_CLOSE
        self.to_map = to_map
        self.to_pos = to_pos

    def map_setting(self, block_array, spawn_list, char_array):
        self.blocks.extend(entity.board(self, block_array))
        self.spawn_list = spawn_list
        self.characters.extend(char_array)

    def add_block(self, *block):
        for b in block:
            self.blocks.append(b)

    def start(self, game_runner, player, pos):
        self.game_runner = game_runner
        self.player = player
        self.player.replace(pos)
        self.cam = camera.camera(self.player)
        self.cam.set_x_limit(-self.size_tiles[0]*entity.TILE_SIZE+size[0]-200, 200)
        self.cam.set_y_limit(-self.size_tiles[1]*entity.TILE_SIZE+size[1]-200, 200)
        self.cam.replace(-player.pos[0]+size[0]/2, -player.pos[1]+size[1]/2)
        self.player.set_map(self)
        self.transition_type = TRANSITION_OPEN
    
    def update(self):
        # THINGS TO UPDATE:
        #   PLAYER
        #   EFFECTS
        #   CAMERA
        #   BLOCKS
        # EVENT MANIPULATION

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.game_runner.done = True  # Flag that we are done so we exit loop
            if event.type == pygame.KEYDOWN:
                if event.key == self.player.keyset['UP']:  # key 'w'
                    self.player.keydown['UP'] = True
                    self.player.face = 1.5
                elif event.key == self.player.keyset['LEFT']:  # key 'a'
                    self.player.keydown['LEFT'] = True
                    self.player.face = 1
                elif event.key == self.player.keyset['DOWN']:  # key 's'
                    self.player.keydown['DOWN'] = True
                    self.player.face = 0.5
                elif event.key == self.player.keyset['RIGHT']:  # key 'd'
                    self.player.keydown['RIGHT'] = True
                    self.player.face = 0
            if event.type == pygame.KEYUP:
                if event.key == self.player.keyset['UP']:  # key 'w'
                    self.player.keydown['UP'] = False
                elif event.key == self.player.keyset['LEFT']:  # key 'a'
                    self.player.keydown['LEFT'] = False
                elif event.key == self.player.keyset['DOWN']:  # key 's'
                    self.player.keydown['DOWN'] = False
                elif event.key == self.player.keyset['RIGHT']:  # key 'd'
                    self.player.keydown['RIGHT'] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.player.mousedown['LEFT'] = True
                if event.button == 3:
                    self.player.mousedown['RIGHT'] = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.player.mousedown['LEFT'] = False
                if event.button == 3:
                    self.player.mousedown['RIGHT'] = False
            if event.type == pygame.MOUSEMOTION:
                input_pos = self.cam.coord_display_into_gameworld(event.pos)
                if input_pos[0] != self.player.get_center()[0]:
                    if input_pos[0]-self.player.get_center()[0] > 0:
                        self.player.mouse_angle = numpy.arctan( (input_pos[1]-self.player.get_center()[1])/(input_pos[0]-self.player.get_center()[0]) ) / numpy.pi
                    if input_pos[0]-self.player.get_center()[0] < 0:
                        self.player.mouse_angle = numpy.arctan( (input_pos[1]-self.player.get_center()[1])/(input_pos[0]-self.player.get_center()[0]) ) / numpy.pi + 1
                    
                if input_pos[0] == self.player.get_center()[0]:
                    if input_pos[1]-self.player.get_center()[1] > 0:
                        self.player.mouse_angle = 1/2
                    if input_pos[1]-self.player.get_center()[1] < 0:
                        self.player.mouse_angle = -1/2

        # PLAYER UPDATE
        self.player.update()

        # EFFECTS UPDATE
        for e in effect.whole:
            e.update()

        # CAMERA MOVEMENT
        self.cam.update()
        
        # BLOCKS UPDATE
        for b in self.blocks:
            b.update()

        # CARPETS UPDATE
        for ca in self.carpets:
            ca.update()
            self.carpets.remove(ca)

        # DARKNESS UPDATE
        for l in self.lights:
            l.update()

        # UI UPDATE
        self.UI.update()

        # MAP TRANSITION
        if self.transition_type == TRANSITION_CLOSE and self.transition_tick == self.transition_delay:
            self.player.replace((99999,99999))
            self.game_runner.map_change(self.to_map, self.to_pos)

        

    def render(self):
        # THINGS TO RENDER:
        #   BACKGROUND
        #   BLOCKS
        #   EFFECTS
        #   PLAYER
        #   UI

        # BACKGROUND RENDER
        screen.blit(self.image_background, (int(self.cam.offset[0]), int(self.cam.offset[1])))

        # BLOCKS RENDER
        for b in self.blocks:
            b.render()
        
        # CHARACTERS RENDER
        for ch in self.characters:
            ch.render()

        # PLAYER RENDER
        self.player.render()
        if self.player.action != None:
            self.player.action.render()
        
        # EFFECTS RENDER
        for e in effect.whole:
            e.render()

        # CARPETS RENDER
        for ca in self.carpets:
            ca.render()

        # DARKNESS RENDER
        darkness = pygame.Surface(size)
        darkness.fill((0,0,0))
        darkness.set_alpha(int(255*self.darkness))
        for l in self.lights:
            pygame.draw.polygon(darkness, (60,60,60), l.points(self.cam.offset))
        darkness.set_colorkey((60,60,60))
        
        #   blur darkness
        darkness_str = pygame.image.tostring(darkness, "RGBA", False)
        pil_blured = Image.frombytes("RGBA", darkness.get_size(), darkness_str).filter(ImageFilter.GaussianBlur(radius=6))
        darkness = pygame.image.fromstring(pil_blured.tobytes("raw", "RGBA"), darkness.get_size(), "RGBA")

        
        
        screen.blit(darkness, (0,0))
        


        # UI RENDER
        self.UI.render()

        # SCREEN EFFECT RENDER
        #   TRANSITION OPEN
        if self.transition_type == TRANSITION_OPEN:
            self.effect_screen.fill(BLACK)
            pygame.draw.circle(self.effect_screen, (60,60,60), (int(self.player.pos[0]+self.cam.offset[0]), int(self.player.pos[1]+self.cam.offset[1])), int(800/self.transition_delay*self.transition_tick), 0)
            self.effect_screen.set_colorkey((60,60,60))
            screen.blit(self.effect_screen, (0,0))
            self.transition_tick += 1
            if self.transition_tick == self.transition_delay:
                self.transition_type = TRANSITION_NONE
                self.transition_tick = 0
        
        #   TRANSITION CLOSE
        if self.transition_type == TRANSITION_CLOSE:

            self.effect_screen.fill(BLACK)
            pygame.draw.circle(self.effect_screen, (60,60,60), (int(self.player.pos[0]+self.cam.offset[0]), int(self.player.pos[1]+self.cam.offset[1])), 800 - int(800/self.transition_delay*self.transition_tick), 0)
            self.effect_screen.set_colorkey((60,60,60))
            screen.blit(self.effect_screen, (0,0))
            self.transition_tick += 1



#-- TEST BENCH ------------------------------------------------------------------------------#

if __name__ == "__main__":

    map_now = mapping(player, (40, 24))
    map_now.map_setting(map_temp, {'start': (50,300)})
    map_now.background_setting(pygame.image.load("img/background.png"))
    map_now.start(player, map_now.spawn_list['start'])
    map_now.add_block( entity.eventblock(map_now, (5,5), entity.PLAYER_COLLIDE, lambda: map_now.player.harms.append(attack.damage(5, False))) )
    map_now.add_block( entity.eventblock(map_now, (10,5), entity.PLAYER_COLLIDE, lambda: map_now.player.set_acc((3,3), 10)) )
    map_now.add_block( entity.eventblock(map_now, (15,5), entity.PLAYER_COLLIDE, lambda: map_now.player.set_controlled('stunned', 30)) )
    map_now.add_block( entity.eventblock(map_now, (20,5), entity.PLAYER_COLLIDE, lambda: map_now.player.set_controlled('exhaust', 30)) )
    map_now.add_block( entity.eventblock(map_now, (25,5), entity.PLAYER_COLLIDE, lambda: map_now.player.set_controlled('airborne', 10)) )
    map_now.add_block( entity.eventblock(map_now, (30,5), entity.PLAYER_COLLIDE, lambda: map_now.player.set_disorder('poisoned', 30, 1)) )
    map_now.add_block( entity.eventblock(map_now, (35,5), entity.PLAYER_COLLIDE, lambda: map_now.player.set_disorder('burning', 300, 0.1)) )
    

    import entity

    clock = pygame.time.Clock()

    done = False
    
    while not done:

        clock.tick(30)  # 게임의 화면 투사를 30Hz로 설정

        #-- UPDATE FUNCTION ------------------------------------------------------------------------------#
        map_now.update()    # Update Map

        #-- REDNER FUNCTION ------------------------------------------------------------------------------#
        screen.fill(BLACK)
        map_now.render()

        pygame.display.flip()
            
    quit()



