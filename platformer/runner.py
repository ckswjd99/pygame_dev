from setting import *
import map

class runner:
    def __init__(self, player, start_map):
        self.player = player
        self.map_now = start_map
    
    def run(self):
        clock = pygame.time.Clock()

        done = False

        while not done:

            clock.tick(30)  # 게임의 화면 투사를 30Hz로 설정

            #-- UPDATE FUNCTION ------------------------------------------------------------------------------#
            self.map_now.update()    # Update Map
            #print(cam.offset)

            #-- REDNER FUNCTION ------------------------------------------------------------------------------#
            screen.fill(BLACK)
            self.map_now.render()

            pygame.display.flip()

game_run = runner(player, map.maps['test_map'])

if __name__ == "__main__":
    game_run.run()