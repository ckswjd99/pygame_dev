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
    
    def run(self):

        self.done = False

        self.player.set_map(self.map_now)
        self.map_now.start(self, self.player, self.map_now.spawn_list['start'])

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
        sys.exit()

    def map_change(self, map_new, pos_new):
        transition_tick = 20

        for i in range(transition_tick):
            clock.tick(FPS)
            self.map_now.effect_screen.fill(BLACK)
            pygame.draw.circle(self.map_now.effect_screen, (60,60,60), (100,100), 1200 - int(1200/transition_tick*i), 0)
            self.map_now.effect_screen.set_colorkey((60,60,60))
            screen.blit(self.map_now.effect_screen, (0,0))
            pygame.display.flip()
        
        self.map_now = map_new
        self.player.set_map(map_new)
        self.map_now.start(self, self.player, pos_new)
        
        for i in range(transition_tick):
            print("IH")
            clock.tick(FPS)
            self.map_now.effect_screen.fill(BLACK)
            pygame.draw.circle(self.map_now.effect_screen, (60,60,60), (100,100), int(1200/transition_tick*i), 0)
            self.map_now.effect_screen.set_colorkey((60,60,60))
            screen.blit(self.map_now.effect_screen, (0,0))
            pygame.display.flip()




#-- GENERATE PLAYER ------------------------------------------------------------------------------#
import character as ch
player_bstat = ch.basic_stat(acc=3, jump_power=10, max_speed=10, max_hp=100, max_mp=100)
player_phstat = ch.physics_stat(width=20, height=20, air_drag=0.2)
player = ch.player("1P", (500,400), player_bstat, player_phstat)


if __name__ == "__main__":
    from runner_setting import *
    game_run = runner(player, maps['test_map2'])
    game_run.run()
    game_run.map_change(maps['test_map2'], maps['test_map2'].spawn_list['start'])
    