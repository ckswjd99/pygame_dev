from setting import *
import pygame.gfxdraw
from numpy import cos, sin, pi


#---------- Root Class: particle ----------#

class particle:
    def __init__(self, eff, pos, life):
        self.eff = eff;
        self.eff.particles.append(self)
        self.pos = pos
        self.life = life
        self.life_left = life
        
    def update(self):
        pass
    
    def render(self):
        pass

    def demol(self):
        for p in self.eff.particles:
            if p == self:
                self.eff.particles.remove(p)
    pass



#---------- Children Class: SPARKS ----------#

class spark_circle(particle):
    def __init__(self, eff, pos, life, speed, angle, size, color):
        particle.__init__(self, eff, pos, life)
        self.speed = speed
        self.angle = angle
        self.size = size
        self.color = color
        
    def update(self):
        self.pos = (int(self.pos[0] + self.speed*cos(self.angle*pi)*(self.life_left/self.life)), int(self.pos[1] + self.speed*sin(self.angle*pi)*(self.life_left/self.life)))
        self.life_left -= 1

        if self.life_left == 0:
            self.demol()
        
    def render(self):
        pygame.gfxdraw.filled_circle(screen, self.pos[0]+cam.offset[0], self.pos[1]+cam.offset[1], self.size, pygame.Color(self.color[0], self.color[1], self.color[2], int(255*(self.life_left/self.life))))

class spark_rectangle(particle):
    def __init__(self, eff, pos, life, speed, angle, size, color):
        particle.__init__(self, eff, pos, life)
        self.speed = speed
        self.angle = angle
        self.size = size
        self.color = color
        
    def update(self):
        self.pos = (int(self.pos[0] + self.speed*cos(self.angle*pi)*(self.life_left/self.life)), int(self.pos[1] + self.speed*sin(self.angle*pi)*(self.life_left/self.life)))
        self.life_left -= 1

        if self.life_left == 0:
            self.demol()
        
    def render(self):
        pygame.gfxdraw.box(screen, pygame.Rect(self.pos[0]-self.size/2+cam.offset[0], self.pos[1]-self.size/2+cam.offset[1], self.size, self.size), pygame.Color(self.color[0], self.color[1], self.color[2],int(255*(self.life_left/self.life))))



#---------- Children Class: SPARKS with gravity ----------#

class spark_gravity_circle(particle):
    def __init__(self, eff, pos, life, gravity, speed, angle, size, color):
        particle.__init__(self, eff, pos, life)
        self.gravity = gravity
        self.speed = speed
        self.angle = angle
        self.size = size
        self.color = color
        
    def update(self):
        self.pos = (int(self.pos[0] + self.speed*cos(self.angle*pi)*(self.life_left/self.life) + self.gravity[0]*(self.life - self.life_left)), int(self.pos[1] + self.speed*sin(self.angle*pi)*(self.life_left/self.life) + self.gravity[1]*(self.life - self.life_left)))
        self.life_left -= 1

        if self.life_left == 0:
            self.demol()
        
    def render(self):
        pygame.gfxdraw.filled_circle(screen, self.pos[0]+cam.offset[0], self.pos[1]+cam.offset[1], self.size, pygame.Color(self.color[0], self.color[1], self.color[2], int(255*(self.life_left/self.life))))
        
class spark_gravity_rectangle(particle):
    def __init__(self, eff, pos, life, gravity, speed, angle, size, color):
        particle.__init__(self, eff, pos, life)
        self.gravity = gravity
        self.speed = speed
        self.angle = angle
        self.size = size
        self.color = color
        
    def update(self):
        self.pos = (int(self.pos[0] + self.speed*cos(self.angle*pi)*(self.life_left/self.life)) + self.gravity[0]*(self.life - self.life_left), int(self.pos[1] + self.speed*sin(self.angle*pi)*(self.life_left/self.life)) + self.gravity[1]*(self.life - self.life_left))
        self.life_left -= 1

        if self.life_left == 0:
            self.demol()
        
    def render(self):
        pygame.gfxdraw.box(screen, pygame.Rect(self.pos[0]-self.size/2+cam.offset[0], self.pos[1]-self.size/2+cam.offset[1], self.size, self.size), pygame.Color(self.color[0], self.color[1], self.color[2],int(255*(self.life_left/self.life))))



#---------- Children Class: WAVES ----------#

class wave_circle(particle):
    def __init__(self, eff, pos, life, speed, size, color):
        particle.__init__(self, eff, pos, life)
        self.speed = speed
        self.size = size
        self.color = color

    def update(self):
        self.size += self.speed
        self.life_left -= 1
        if self.life_left == 0:
            self.demol()

    def render(self):
        pygame.gfxdraw.aacircle(screen, self.pos[0]+cam.offset[0], self.pos[1]+cam.offset[1], self.size, pygame.Color(self.color[0], self.color[1], self.color[2], int(255*(self.life_left/self.life))))

class wave_rectangle(particle):
    def __init__(self, eff, pos, life, speed, size, color):
        particle.__init__(self, eff, pos, life)
        self.speed = speed
        self.size = size
        self.color = color

    def update(self):
        self.size += self.speed
        self.life_left -= 1
        if self.life_left == 0:
            self.demol()

    def render(self):
        pygame.gfxdraw.rectangle(screen, pygame.Rect(self.pos[0]-self.size/2+cam.offset[1], self.pos[1]-self.size/2+cam.offset[0], self.size, self.size), pygame.Color(self.color[0], self.color[1], self.color[2],int(255*(self.life_left/self.life))))



#---------- Children Class: GAS ----------#

class gas_circle(particle):
    def __init__(self, eff, pos, life, speed, angle, size, color):
        particle.__init__(self, eff, pos, life)
        self.speed = speed
        self.angle = angle
        self.size = size
        self.color = color
        
    def update(self):
        self.pos = (int(self.pos[0] + self.speed*cos(self.angle*pi)*(self.life_left/self.life)), int(self.pos[1] + self.speed*sin(self.angle*pi)*(self.life_left/self.life)))
        self.life_left -= 1
        if self.life_left == 0:
            self.demol()
    
    def render(self):
        pygame.gfxdraw.filled_circle(screen, self.pos[0]+cam.offset[0], self.pos[1]+cam.offset[1], int(self.size*(self.life_left/self.life)), self.color)














