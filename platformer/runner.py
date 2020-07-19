from setting import *

class runner:
    def __init__(self, player, map_first):
        self.player = player
        self.map_now = map_first
    
    def run(self):

        clock = pygame.time.Clock()

        done = False

        self.player.set_map(self.map_now)
        self.map_now.start(self, self.player, self.map_now.spawn_list['start'])

        while not done:

            clock.tick(30)  # 게임의 화면 투사를 30Hz로 설정

            #-- UPDATE FUNCTION ------------------------------------------------------------------------------#
            self.map_now.update()    # Update Map
            #print(cam.offset)

            #-- REDNER FUNCTION ------------------------------------------------------------------------------#
            screen.fill(BLACK)
            self.map_now.render()

            pygame.display.flip()

    def map_change(self, map_new, pos_new):
        self.map_now = map_new
        self.player.set_map(map_new)
        self.map_now.start(self, self.player, pos_new)

def get_runner():
    return game_run



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
    