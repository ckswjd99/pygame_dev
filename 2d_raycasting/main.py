from setting import *

import ray, poly
import pygame
import numpy

#MAIN RENDER FUNC
def render():
    screen.fill(BLACK)
    
    for r in ray.ray_source_whole:
        r.render()
        
    for p in poly.whole:
        p.render()
    

#MAIN UPDATE FUNC
def update():
    for r in ray.ray_source_whole:
        r.update()
        
    render()

#메인 루프
def mainloop():
    
    done = False
    clock = pygame.time.Clock()

    src_x = 500
    src_y = 400

    keyUP = False
    keyLEFT = False
    keyDOWN = False
    keyRIGHT = False

    ray_num = 200
    ray.ray_source((src_x,src_y), 0, 1/4, 30)

    poly.poly([(100, 200), (200, 100)], WHITE)
    poly.poly([(100, 200), (0, 200)], WHITE)
    poly.poly([(700, 400), (700, 500), (800, 500), (800, 400)], WHITE)
    poly.poly([(900, 400), (900, 500), (1000, 500), (1000, 400)], WHITE)
    poly.poly([(300, 300), (400, 350), (400, 400), (500, 450), (500, 500), (300, 500)], WHITE)

    speed = 5
    
    while not done:
        clock.tick(FPS) #게임의 화면 투사를 30Hz로 설정
        
        #이벤트 입력받기
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            if event.type == pygame.MOUSEMOTION:
                angle_new = 0
                if event.pos[0] == src_x and event.pos[1] - src_y == 0:
                    angle_new = 0
                elif event.pos[0] == src_x and event.pos[1] - src_y > 0:
                    angle_new = numpy.pi * 1/2
                elif event.pos[0] == src_x and event.pos[1] - src_y < 0:
                    angle_new = numpy.pi * 3/2
                elif event.pos[0] < src_x:
                    angle_new = numpy.arctan((event.pos[1] - src_y) / (event.pos[0] - src_x)) + numpy.pi
                else:
                    angle_new = numpy.arctan((event.pos[1] - src_y) / (event.pos[0] - src_x))
                for r in ray.ray_source_whole:
                    r.update_angle(angle_new / numpy.pi)
            if event.type == pygame.KEYDOWN:
                if event.key == 119:    #key 'w'
                    keyUP = True
                elif event.key == 97:   #key 'a'
                    keyLEFT = True
                elif event.key == 115:  #key 's'
                    keyDOWN = True
                elif event.key == 100:  #key 'd'
                    keyRIGHT = True
            if event.type == pygame.KEYUP:
                if event.key == 119:  # key 'w'
                    keyUP = False
                elif event.key == 97:  # key 'a'
                    keyLEFT = False
                elif event.key == 115:  # key 's'
                    keyDOWN = False
                elif event.key == 100:  # key 'd'
                    keyRIGHT = False

        if keyUP:
            src_y -= speed
        if keyLEFT:
            src_x -= speed
        if keyDOWN:
            src_y += speed
        if keyRIGHT:
            src_x += speed

        for r in ray.ray_source_whole:
            r.update_pos( (src_x, src_y) )
        
        update()    #call update funtion
        
        pygame.display.flip()

if __name__ == "__main__":
    mainloop()

quit()
