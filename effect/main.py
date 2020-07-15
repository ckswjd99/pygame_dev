import effect
import pygame
from setting import *

#MAIN RENDER FUNC
def render():
    screen.fill(BLACK)
    
    for e in effect.whole:
        e.render()

#MAIN UPDATE FUNC
def update():
    for e in effect.whole:
        e.update()
        
    render()

#메인 루프
def mainloop():
    
    done = False
    clock = pygame.time.Clock()
    
    lastkey = 0
    
    while not done:
        clock.tick(FPS) #게임의 화면 투사를 30Hz로 설정
        
        #이벤트 입력받기
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEBUTTONDOWN:
                if lastkey == 49:
                    effect.spark_circle(event.pos, 10, 4, 5, pygame.Color(0,255,0), 8)
                elif lastkey == 50:
                    effect.spark_rectangle(event.pos, 10, 5, 10, pygame.Color(0,255,0), 8)
                elif lastkey == 51:
                    effect.spark_gravity_circle(event.pos, 10, (0,2), 4, 5, pygame.Color(0,255,0), 8)
                elif lastkey == 52:
                    effect.spark_gravity_rectangle(event.pos, 10, (0,2), 5, 10, pygame.Color(0,255,0), 8)
                elif lastkey == 53:
                    effect.fountain_circle(event.pos, 10, 3, 5, 6, pygame.Color(255,0,0), 3, effect.kill_MOUSEBUTTONUP)
                elif lastkey == 54:
                    effect.fountain_rectangle(event.pos, 10, 3, 5, 12, pygame.Color(255,0,0), 3, effect.kill_MOUSEBUTTONUP)
                elif lastkey == 55:
                    effect.fountain_gravity_circle(event.pos, 10, (0,1.5), 3, 5, 6, pygame.Color(255,0,0), 3, effect.kill_MOUSEBUTTONUP)
                elif lastkey == 56:
                    effect.fountain_gravity_rectangle(event.pos, 10, (0,1.5), 3, 5, 12, pygame.Color(255,0,0), 3, effect.kill_MOUSEBUTTONUP)
                elif lastkey == 57:
                    effect.wave_circle(event.pos, 10, 5, 10, pygame.Color(255,255,255))
                elif lastkey == 48:
                    effect.gas_circle(event.pos, 10, 4, 10, pygame.Color(0,255,0), 8)
                
            if event.type == pygame.MOUSEBUTTONUP:
                for e in effect.kill_MOUSEBUTTONUP:
                    e.kill()
            if event.type == pygame.KEYDOWN:
                lastkey = event.key
                print(event.key)
        
        update()    #call update funtion
        
        pygame.display.flip()

if __name__ == "__main__":
    mainloop()

quit()
