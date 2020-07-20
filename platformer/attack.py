import pygame
from setting import *

#---------- CONSTANTS ----------#
PHYSICAL = 0
MAGICAL = 1
NORMAL = 2
POISON = 3
FIRE = 4





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

