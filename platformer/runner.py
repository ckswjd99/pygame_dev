############################## README ############################################################
##  This file is for class 'runner'.
## 
##  runner class runs main loop of gameplay.
##  
##  runner class contains following attributes:
##    > player      : defined outside and passed when runner class is initialized.
##    > map_now     : runner class operates this map_now map.
##  
##  and following functions:
##    > __init__(self, player, map_first)   : init function.
##    > run(self)                           : runs main loop.
##    > map_change(self, map_new, pos_new)  : changes map_now with player in position pos_new.
##  
##################################################################################################

from setting import *
import sys

clock = pygame.time.Clock()

class runner:
    def __init__(self, player, map_first):
        self.player = player
        self.map_now = map_first
        self.done = False

        self.player.set_map(self.map_now)
        self.map_now.start(self, self.player, self.map_now.spawn_list['start'])
    
    def run(self):

        while not self.done:

            clock.tick(FPS)  # 게임의 화면 투사를 30Hz로 설정

            #-- UPDATE FUNCTION ------------------------------------------------------------------------------#
            self.map_now.update()    # Update Map
            #print(cam.offset)

            #-- REDNER FUNCTION ------------------------------------------------------------------------------#
            screen.fill(BLACK)
            self.map_now.render()

            pygame.display.flip()
        
        # END GAME
        pygame.quit()
        #quit()

    def map_change(self, map_new, pos_new):
        self.map_now = map_new
        self.player.set_map(map_new)
        self.map_now.start(self, self.player, pos_new)


if __name__ == "__main__":
    from runner_setting import *
    game_run = runner(player, maps['test_map2'])
    game_run.run()
    game_run.map_change(maps['test_map2'], maps['test_map2'].spawn_list['start'])
    
