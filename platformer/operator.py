from setting import *
import map


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