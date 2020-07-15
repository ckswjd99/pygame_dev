from setting import *
import pygame, numpy
import pygame.gfxdraw

line_whole = []
poly_whole = []


#---------- CLASS: Line ----------#

class line:
    def __init__(self, pos0, pos1):
        self.pos0 = pos0
        self.pos1 = pos1
        line_whole.append(self)
    
    def render(self):
        pygame.gfxdraw.line(screen, self.pos0[0], self.pos0[1], self.pos1[0], self.pos1[1], WHITE)
        
    def demol(self):
        line_whole.remove(self)
        

#---------- CLASS: Poly ----------#

class poly:
    def __init__(self, pos, color):
        self.pos = pos
        self.lines = []
        for i in range(len(pos)):
            if i == len(pos)-1:
                self.lines.append(line( pos[i], pos[0] ))
            else:
                self.lines.append(line( pos[i], pos[i+1] ))
                
        self.color = color
        poly_whole.append(self)
    
    def render(self):
        pygame.gfxdraw.aapolygon(screen, self.pos, self.color)
        
    def demol(self):
        for l in self.lines:
            l.demol()
        poly_whole.remove(self)


#---------- TEST BENCH ----------#
if __name__ == "__main__":
    line( (100,100), (0,200) )
    line( (0,200), (0,300) )
    for l in line_whole:
        l.render()
    poly( [(300,300), (600,300), (500,600)], WHITE )
    for p in poly_whole:
        p.render()
    pygame.display.flip()
