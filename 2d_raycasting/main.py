from setting import *

import ray, poly
import pygame

#MAIN RENDER FUNC
def render():
    screen.fill(BLACK)
    
    for r in ray.whole:
        r.render()
        
    for p in poly.whole:
        p.render()
    

#MAIN UPDATE FUNC
def update():
    for r in ray.whole:
        r.update()
        
    render()

#메인 루프
def mainloop():
    
    done = False
    clock = pygame.time.Clock()
    
    while not done:
        clock.tick(FPS) #게임의 화면 투사를 30Hz로 설정
        
        #이벤트 입력받기
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEMOTION:
                for r in ray.whole:
                    r.update_pos(event.pos)
        
        update()    #call update funtion
        
        pygame.display.flip()

if __name__ == "__main__":
    mainloop()

quit()
