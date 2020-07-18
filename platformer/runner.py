from setting import *
import mapping

class runner:
    def __init__(self, player, start_map):
        self.player = player
        self.map_now = start_map
    
    def run(self):
        clock = pygame.time.Clock()

        done = False

        self.map_now.start(self.player, self.map_now.spawn_list['start'])

        while not done:

            clock.tick(30)  # 게임의 화면 투사를 30Hz로 설정

            #-- UPDATE FUNCTION ------------------------------------------------------------------------------#
            self.map_now.update()    # Update Map
            #print(cam.offset)

            #-- REDNER FUNCTION ------------------------------------------------------------------------------#
            screen.fill(BLACK)
            self.map_now.render()

            pygame.display.flip()

game_run = runner(player, mapping.maps['test_map2'])

if __name__ == "__main__":
    game_run.run()