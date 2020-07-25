from setting import *
import pygame
from numpy import *
import pygame.gfxdraw
from util import *

import poly

#---------- CLASS: Ray ----------#

class ray:
    def __init__(self, ray_source, pos, angle, max_dist):
        self.ray_source = ray_source
        self.pos = pos
        self.angle = angle
        self.max_dist = max_dist
        self.max_pos = ( int(pos[0] + self.max_dist * cos(self.angle * pi)), int(pos[1] + self.max_dist * sin(self.angle * pi)) )
        self.end_pos = self.max_pos
        self.touch = False
    
    def update(self):
        # update endpoint of ray
        self.end_pos = self.max_pos
        for b in self.ray_source.map.blocks:
            if b.collision_ray == True:
                lines = [poly.line((b.poly.x,b.poly.y), (b.poly.x+b.poly.w,b.poly.y)), poly.line((b.poly.x+b.poly.w,b.poly.y), (b.poly.x+b.poly.w,b.poly.y+b.poly.h)), poly.line((b.poly.x+b.poly.w,b.poly.y+b.poly.h), (b.poly.x,b.poly.y+b.poly.h)), poly.line((b.poly.x,b.poly.y+b.poly.h), (b.poly.x,b.poly.y))]
                for line in lines:
                    c_point = crossing_point(line.pos0, line.pos1, self.pos, self.max_pos )
                    if c_point == False:
                        continue
                    if points_in_line( line.pos0, c_point, line.pos1 ) == True and points_in_line( self.pos, c_point, self.max_pos ):
                        if distance_between(self.pos, c_point) < distance_between(self.pos, self.end_pos):
                            self.end_pos = ( int(c_point[0]), int(c_point[1]) ) # ray touched sth
                            self.touch = line
    
    def update_pos(self, pos):
        self.pos = pos
        self.max_pos = ( int(pos[0] + self.max_dist * cos(self.angle * pi)), int(pos[1] + self.max_dist * sin(self.angle * pi)) )
        self.end_pos = self.max_pos

    def update_angle(self, angle):
        self.angle = angle
        self.max_pos = ( int(self.pos[0] + self.max_dist * cos(angle * pi)), int(self.pos[1] + self.max_dist * sin(angle * pi)) )
        self.end_pos = self.max_pos

    def render(self):
        pygame.gfxdraw.line(screen, self.pos[0], self.pos[1], self.end_pos[0], self.end_pos[1], WHITE)



#---------- CLASS: Ray Source ----------#

class ray_source:
    def __init__(self, map, pos, angle, angle_range, distance, num):
        self.map = map
        self.pos = pos
        self.angle = angle
        self.angle_range = angle_range
        self.distance = distance
        self.num = num

        self.rays = []
        for i in range(num):
            self.rays.append( ray(self, pos, angle-angle_range/2+angle_range/(num-1)*i, distance) )

    def points(self, offset):
        result = []
        for r in self.rays:
            result.append((r.end_pos[0]+offset[0], r.end_pos[1]+offset[1]))
        return result

    def update(self):
        for r in self.rays:
            r.update()

    def update_pos(self, pos):
        for r in self.rays:
            r.update_pos(pos)

    def update_angle(self, angle):
        for i in range(self.num):
            self.rays[i].update_angle(angle-self.angle_range/2+self.angle_range/(self.num-1)*i)

    def render(self):
        for r in self.rays:
            r.render()




#---------- TEST BENCH ----------#
if __name__ == "__main__":
    temp = crossing_point( (1,0), (-1,0), (0,1), (0,-1) )
    print(temp)
    temp = distance_between( (1,1), (-1,-1) )
    print(temp)
    temp = points_in_line( (0,0), (100,100), (200,200) )
    print(temp)
    temp = points_in_line( (0,0), (100,100), (200,205) )
    print(temp)
    
    offset = (500,400)
    ray_num = 50
    for i in range(ray_num):
        ray( offset, 2/ray_num*i, 10000 )
        
    poly.poly( [(100,200), (200,100)], WHITE )
    poly.poly( [(100,200), (0,200)], WHITE )
    poly.poly( [(700,400), (700,500), (800,500), (800,400)], WHITE)
    poly.poly( [(900,400), (900,500), (1000,500), (1000,400)], WHITE)
    poly.poly( [(300,300), (400,350), (400,400), (500,450), (500,500), (300,500)], WHITE)
    
    for r in whole:
        r.update()
    
    for r in whole:
        r.render()
    for p in poly.whole:
        p.render()
    
    pygame.display.flip()