from setting import *
import pygame, numpy
import pygame.gfxdraw

whole = []


#---------- CLASS: Line ----------#

class line:
    def __init__(self, pos0, pos1):
        self.pos0 = pos0
        self.pos1 = pos1
    
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
        whole.append(self)
    
    def render(self):
        
        if len(self.pos) == 0:
            pass
        elif len(self.pos) == 1:
            pass
        elif len(self.pos) == 2:
            pygame.gfxdraw.line(screen, self.pos[0][0], self.pos[0][1], self.pos[1][0], self.pos[1][1], self.color)
        else:
            pygame.gfxdraw.polygon(screen, self.pos, self.color)    # if use aapolygon, some lines are missing. reason unknown.
        
    def demol(self):
        for l in self.lines:
            l.demol()
        whole.remove(self)


#---------- TEST BENCH ----------#
if __name__ == "__main__":
    poly( [(100,100), (0,200)], WHITE )
    poly( [(0,200), (0,300)], WHITE )
    #poly( [(300,300), (600,300), (500,600)], WHITE )
    poly( [(300,300), (600,300), (500,600), (300,600)], WHITE )
    for p in whole:
        p.render()
    pygame.display.flip()
