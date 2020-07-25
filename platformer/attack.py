import pygame
import numpy
from setting import *

#---------- CONSTANTS FOR TYPE ----------#
PHYSICAL    = 0
MAGICAL     = 1
NORMAL      = 2
POISON      = 3
FIRE        = 4

#---------- CONSTANTS FOR SKILL STATE----------#
READY       = 0
ACTION      = 1
END         = 2





#-- DAMAGE CLASS ------------------------------------------------------------------------------#
class damage:
    def __init__(self, amount, kind):
        self.amount = amount
        self.type = kind


#-- CARPET CLASS ------------------------------------------------------------------------------#
class carpet:
    def __init__(self, pos, hitbox, damage, target_num, performer, ignore):
        self.pos = pos
        self.hitbox = hitbox
        self.damage = damage
        self.target_num = target_num
        self.performer = performer
        self.ignore = ignore

    def find_target(self):
        result = []
        
        for ch in self.performer.map.characters:
            if self.hitbox.colliderect(ch.poly) and self.ignore.count(ch) == 0:
                print(ch)
                result.append(ch)
        
        if self.hitbox.colliderect(self.performer.map.player.poly) and self.ignore.count(self.performer.map.player) == 0:
            result.append(self.performer.map.player)
        
        if self.target_num > 0 and len(result) > 0:
            while len(result) > self.target_num:
                fartherest = result[0]
                for t_ch in result:
                    if (t_ch.pos[0]-self.pos[0])**2 + (t_ch.pos[1]-self.pos[1])**2 > (fartherest.pos[0]-self.pos[0])**2 + (fartherest.pos[1]-self.pos[1])**2:
                        fartherest = t_ch
                result.remove(fartherest)
        
        return result

    def update(self):
        target = self.find_target()
        for t in target:
            t.damaged(self.damage)

    def render(self):
        cam_rect = self.hitbox.copy()
        cam_rect.move_ip(self.performer.map.cam.offset[0], self.performer.map.cam.offset[1])
        pygame.draw.rect(screen, RED, cam_rect)


#-- SKILL CLASS ------------------------------------------------------------------------------#
class skill:
    def __init__(self, performer):
        self.performer = performer
        self.state = READY
        self.charge = 0

    def set_state(self, state):
        self.state = state
    
    def update(self):
        pass

    def render(self):
        pass


#-- PLAIN ATTACK CLASS ------------------------------------------------------------------------------#
class plain_attack(skill):
    def __init__(self, performer):
        skill.__init__(self, performer)

        self.tick = 0
        self.is_pushed = False

        self.image = pygame.image.load("img/attack/plain_attack.png")

    def set_is_pushed(self, is_pushed):
        self.is_pushed = is_pushed

    def copy(self):
        return plain_attack(self.performer)

    def update(self):
        if self.is_pushed:
            self.state = READY
        else:
            self.state = ACTION

        if self.state == READY:
            pass
        elif self.state == ACTION:
            # SET CARPET!
            if self.tick == 1:
                center = [0,0]
                center[0] = self.performer.get_center()[0] + 20*numpy.cos(self.performer.face)
                center[1] = self.performer.get_center()[1] + 20*numpy.sin(self.performer.face)
                hitbox = pygame.Rect( (center[0]-10,center[1]-10), (20,20) )
                temp_carpet = carpet(center, hitbox, damage(self.performer.b_stat.physical_power, NORMAL), -1, self.performer, [self.performer])
                self.performer.map.carpets.append( temp_carpet )
            self.tick += 1
            if self.tick > 10:
                self.state = END
            pass
        
        if self.state == END:
            self.performer.action = None
            pass
        print("state", self.state)

    def render(self):
        if 1 < self.tick and self.tick < 7:
            offset = [0,0]
            offset[0] = self.performer.pos[0] + 20*numpy.cos(self.performer.face*numpy.pi) + self.performer.map.cam.offset[0]
            offset[1] = self.performer.pos[1] + 20*numpy.sin(self.performer.face*numpy.pi) + self.performer.map.cam.offset[1]
            newimage = pygame.transform.rotate(self.image, -self.performer.face*180)
            newimage.set_colorkey((0,255,0))
            screen.blit(newimage, offset)
        



