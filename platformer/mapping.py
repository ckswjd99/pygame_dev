from setting import *
import pygame
import entity
import effect
import UI
import character
import attack

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
        print(size_tiles, len(self.blocks))

        self.characters = []

        self.UI = UI.UI(self)

    def background_setting(self, image):
        self.image_background = image

    def map_setting(self, block_array, spawn_list):
        self.blocks.extend(entity.board(self, block_array))
        self.spawn_list = spawn_list

    def add_block(self, *block):
        for b in block:
            self.blocks.append(b)

    def start(self, game_runner, player, pos):
        self.game_runner = game_runner
        self.player = player
        self.player.replace(pos)
        self.cam = camera(self.player)
        self.cam.set_x_limit(-self.size_tiles[0]*entity.TILE_SIZE+size[0]-200, 200)
        self.cam.set_y_limit(-self.size_tiles[1]*entity.TILE_SIZE+size[1]-200, 200)
        self.cam.replace(-player.pos[0]+size[0]/2, -player.pos[1]+size[1]/2)
        self.player.set_map_now(self)
    
    def update(self):
        # THINGS TO UPDATE:
        #   PLAYER
        #   EFFECTS
        #   CAMERA
        #   BLOCKS
        # EVENT MANIPULATION
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == self.player.keyset['UP']:  # key 'w'
                    self.player.keydown['UP'] = True
                elif event.key == self.player.keyset['LEFT']:  # key 'a'
                    self.player.keydown['LEFT'] = True
                elif event.key == self.player.keyset['DOWN']:  # key 's'
                    self.player.keydown['DOWN'] = True
                elif event.key == self.player.keyset['RIGHT']:  # key 'd'
                    self.player.keydown['RIGHT'] = True
            if event.type == pygame.KEYUP:
                if event.key == self.player.keyset['UP']:  # key 'w'
                    self.player.keydown['UP'] = False
                elif event.key == self.player.keyset['LEFT']:  # key 'a'
                    self.player.keydown['LEFT'] = False
                elif event.key == self.player.keyset['DOWN']:  # key 's'
                    self.player.keydown['DOWN'] = False
                elif event.key == self.player.keyset['RIGHT']:  # key 'd'
                    self.player.keydown['RIGHT'] = False

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

        # UI UPDATE
        self.UI.update()

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

        # EFFECTS RENDER
        for e in effect.whole:
            e.render()

        # PLAYER RENDER
        self.player.render()

        # UI RENDER
        self.UI.render()
        



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



