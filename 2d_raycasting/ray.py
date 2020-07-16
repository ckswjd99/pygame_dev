from setting import *
import pygame
from numpy import *
import pygame.gfxdraw

import poly


whole = []


#---------- UTILS ----------#

def distance_between(pos0, pos1):
    x1 = pos0[0]
    x2 = pos1[0]
    y1 = pos0[1]
    y2 = pos1[1]
    
    return sqrt( (x1-x2)**2 + (y1-y2)**2 )

def crossing_point(pos00, pos01, pos10, pos11):
    x1 = pos00[0]
    x2 = pos01[0]
    x3 = pos10[0]
    x4 = pos11[0]
    y1 = pos00[1]
    y2 = pos01[1]
    y3 = pos10[1]
    y4 = pos11[1]
    
    if (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4) == 0 or (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4) == 0:
        print("parallel")
        return False
    
    px = ( (x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) )/( (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4) )
    py = ( (x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) )/( (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4) )
    
    return (px,py)
    
def points_in_line(pos0, pos1, pos2):
    if pos0 == pos1:
        return True
    elif pos1 == pos2:
        return True
    elif pos0 == pos2 and pos0 != pos1:
        return False
        
    err = 2 # allowed error
    vec1 = ( pos1[0] - pos0[0], pos1[1] - pos0[1] )
    dist = distance_between(pos1, pos2)
    vec1 = ( vec1[0] / distance_between( (0,0), vec1 ) * dist, vec1[1] / distance_between( (0,0), vec1 ) * dist )
    pos2_go = ( pos1[0] + vec1[0], pos1[1] + vec1[1] )
    if distance_between( pos2_go, pos2) < err:
        return True
    else:
        return False


#---------- CLASS: Ray ----------#

class ray:
    def __init__(self, pos, angle, max_dist):
        self.pos = pos
        self.angle = angle
        self.max_dist = max_dist
        self.max_pos = ( int(pos[0] + self.max_dist * cos(self.angle * pi)), int(pos[1] + self.max_dist * sin(self.angle * pi)) )
        self.end_pos = self.max_pos
        whole.append(self)
    
    def update(self):
        # update endpoint of ray
        self.end_pos = self.max_pos
        for p in poly.whole:
            for line in p.lines:
                c_point = crossing_point(line.pos0, line.pos1, self.pos, self.max_pos )
                if c_point == False:
                    continue
                if points_in_line( line.pos0, c_point, line.pos1 ) == True and points_in_line( self.pos, c_point, self.max_pos ):
                    if distance_between(self.pos, c_point) < distance_between(self.pos, self.end_pos):
                        self.end_pos = ( int(c_point[0]), int(c_point[1]) )
    
    def update_pos(self, pos):
        self.pos = pos
        self.max_pos = ( int(pos[0] + self.max_dist * cos(self.angle * pi)), int(pos[1] + self.max_dist * sin(self.angle * pi)) )
        self.end_pos = self.max_pos

    def render(self):
        pygame.gfxdraw.line(screen, self.pos[0], self.pos[1], self.end_pos[0], self.end_pos[1], WHITE)






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