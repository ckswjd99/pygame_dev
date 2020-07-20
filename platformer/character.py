from setting import *
import pygame, pygame.gfxdraw, numpy
import environment as envi
import effect
import poly as polygon
from topology import *
from util import *
import attack

whole = []

#---------- IMAGE FILES ----------#
img_stunned = pygame.image.load("img/character/stunned.png")
img_exhaust = pygame.image.load("img/character/exhaust.png")
img_poisoned = pygame.image.load("img/character/poisoned.png")
img_burning = pygame.image.load("img/character/burning.png")


#---------- INFO CONTAINING CLASS ----------#
class basic_stat:
    def __init__(self, acc, jump_power, max_speed, max_hp, max_mp):
        self.acc = acc
        self.jump_power = jump_power
        self.max_speed = max_speed
        self.max_hp = max_hp
        self.max_mp = max_mp

class physics_stat:
    def __init__(self, width, height, air_drag):
        self.width = width
        self.height = height
        self.air_drag = air_drag


#---------- PRIMITIVE CLASS ----------#
class character:
    def __init__(self, name, pos, b_stat, ph_stat):
        self.name = name
        self.pos = list(pos)
        self.speed = [0,0]
        self.acc_ext = []   # List of accelerations lasting some ticks, form: [(x,y), tick]
        self.b_stat = b_stat
        self.hp = b_stat.max_hp
        self.mp = b_stat.max_mp
        self.ph_stat = ph_stat
        self.harms = []

        self.poly = pygame.Rect(self.pos[0], self.pos[1], self.ph_stat.width, self.ph_stat.height)

        self.controlled = { # Value means ticks left
            'rooted': 0,
            'stunned': 0,
            'airborne': 0,
            'exhaust': 0,
            'blinded': 0
            }
        self.disorder_tick = {  # Value means ticks left
            'poisoned': 0,
            'burning': 0,
            'blinded': 0,
            'slowed': 0
        }
        self.disorder_amount = {
            'poisoned': 0,  # Value means damage per tick
            'burning': 0,   # Value means damage per tick
            'blinded': 0,   # Value means radidus of scope
            'slowed': 0     # Value means percentage of speed loss
        }

        whole.append(self)

        self.footprint_delay = 3
        self.footprint_tick = self.footprint_delay

    def replace(self, pos):
        self.pos = list(pos)
        self.poly = pygame.Rect(self.pos[0], self.pos[1], self.ph_stat.width, self.ph_stat.height)

    def damaged(self, damage):  # Input: attack.damage
        self.harms.append(damage)

    def set_map(self, map):
        self.map = map

    def set_acc(self, accel, tick):
        self.acc_ext.append([accel, tick])

    def set_controlled(self, kind, tick):
        self.controlled[kind] += tick

    def set_disorder(self, kind, tick, amount):
        self.disorder_tick[kind] += tick
        self.disorder_amount[kind] += amount

    def dead(self):
        pass

    def render(self):
        self.image = pygame.image.load("img/character/character.png")
        screen.blit(self.image, (self.pos[0] + self.map.cam.offset[0], self.pos[1] + self.map.cam.offset[1]))


#---------- CHILDREN CLASS: PLAYER ----------#
class player(character):
    def __init__(self, name, pos, b_stat, ph_stat):
        character.__init__(self, name, pos, b_stat, ph_stat)
        self.keyset = {'UP':119, 'LEFT':97, 'DOWN':115, 'RIGHT':100}
        self.keydown = {'UP':False, 'LEFT':False, 'DOWN':False, 'RIGHT':False}
        self.mousedown = {'LEFT':False, 'RIGHT':False}
        self.poly = pygame.Rect(self.pos[0], self.pos[1], self.ph_stat.width, self.ph_stat.height)
        self.image = pygame.image.load("img/character/player.png")
        self.slot_num = [False, False, False, False]
        self.slot_mouse = [False, False]

    def act(self, obj):
        if obj == False:    # Plain Attack
            self.map.carpets.append( attack.carpet( self.pos, pygame.Rect(self.pos[0]-25,self.pos[1]-25,50,50), attack.damage(5, attack.NORMAL), 1, self, [self] ) )
    
    def update(self):
        #-- MOVEMENT ------------------------------------------------------------------------------#

        # SELF ACCELERATION
        accel = [0,0]
        if self.keydown['UP'] == True:
            accel[1] -= self.b_stat.acc
        if self.keydown['LEFT'] == True:
            accel[0] -= self.b_stat.acc
        if self.keydown['DOWN'] == True:
            accel[1] += self.b_stat.acc
        if self.keydown['RIGHT'] == True:
            accel[0] += self.b_stat.acc

        #   RESTRICTION DUE TO DISORDER
        if self.controlled['stunned'] > 0:
            accel = [0,0]
            self.controlled['stunned'] -= 1

        if self.controlled['airborne'] > 0:
            accel = [0,0]
            self.controlled['airborne'] -= 1

        if self.controlled['exhaust'] > 0:
            if abs(accel[0]) < 1:
                accel[0] = 0
            else:
                accel[0] = int(accel[0]/abs(accel[0])*(abs(accel[0])-2))
            if abs(accel[1]) < 1:
                accel[1] = 0
            else:
                accel[1] = int(accel[1]/abs(accel[1])*(abs(accel[1])-2))
            self.controlled['exhaust'] -= 1
        
        #   NORMAL PROSSESS
        if (-1)*self.b_stat.max_speed <= self.speed[0] + accel[0] and self.speed[0] + accel[0] <= self.b_stat.max_speed:
            self.speed[0] += accel[0]
        elif self.speed[0] + accel[0] > self.b_stat.max_speed and self.speed[0] < self.b_stat.max_speed:
            self.speed[0] = self.b_stat.max_speed
        elif self.speed[0] + accel[0] < (-1)*self.b_stat.max_speed and self.speed[0] > (-1)*self.b_stat.max_speed:
            self.speed[0] = (-1)*self.b_stat.max_speed
            
        if (-1)*self.b_stat.max_speed <= self.speed[1] + accel[1] and self.speed[1] + accel[1] <= self.b_stat.max_speed:
            self.speed[1] += accel[1]
        elif self.speed[1] + accel[1] > self.b_stat.max_speed and self.speed[1] < self.b_stat.max_speed:
            self.speed[1] = self.b_stat.max_speed
        elif self.speed[1] + accel[1] < (-1)*self.b_stat.max_speed and self.speed[1] > (-1)*self.b_stat.max_speed:
            self.speed[1] = (-1)*self.b_stat.max_speed
        
        # GRAVITY
        self.speed[0] += envi.gravity[0]
        self.speed[1] += envi.gravity[1]
        
        # EXTERNAL ACCELERATION
        for a in self.acc_ext:
            self.speed[0] += a[0][0]
            self.speed[1] += a[0][1]
            a[1] -= 1
            if a[1] == 0:
                self.acc_ext.remove(a)
        

        # POSITION UPDATE
        #   RESTRICTION DUE TO DISORDER
        if self.controlled['rooted'] > 0:
            self.speed = [0,0]
            self.controlled['rooted'] -= 1
        #   NORMAL PROCESS
        for i in range(numpy.abs(self.speed[0])):
            if self.speed[0] > 0:
                self.pos[0] += 1
            else:
                self.pos[0] -= 1
            self.poly = pygame.Rect(self.pos[0], self.pos[1], self.ph_stat.width, self.ph_stat.height)

            # CHECK AVAILABILITY HERE
            collide = False
            for g in self.map.blocks:
                if self.poly.colliderect(g.poly) == True and g.collision_character == True:
                    collide = True
            if collide == True:
                if self.speed[0] > 0:
                    self.pos[0] -= 1
                else:
                    self.pos[0] += 1
                self.poly = pygame.Rect(self.pos[0], self.pos[1], self.ph_stat.width, self.ph_stat.height)
                break
        
        for i in range(numpy.abs(self.speed[1])):
            if self.speed[1] > 0:
                self.pos[1] += 1
            else:
                self.pos[1] -= 1
            self.poly = pygame.Rect(self.pos[0], self.pos[1], self.ph_stat.width, self.ph_stat.height)

            # CHECK AVAILABILITY HERE
            collide = False
            for g in self.map.blocks:
                if self.poly.colliderect(g.poly) == True and g.collision_character == True:
                    collide = True
            if collide == True:
                if self.speed[1] > 0:
                    self.pos[1] -= 1
                else:
                    self.pos[1] += 1
                self.poly = pygame.Rect(self.pos[0], self.pos[1], self.ph_stat.width, self.ph_stat.height)
                break

        # AIR DRAG FORCE
        self.speed[0] = int(self.speed[0] * (1-self.ph_stat.air_drag))
        self.speed[1] = int(self.speed[1] * (1-self.ph_stat.air_drag))
        
        #-- \MOVEMENT ------------------------------------------------------------------------------#


        #-- ACT ------------------------------------------------------------------------------#

        if self.mousedown['LEFT']:
            self.act(self.slot_mouse[0])
        if self.mousedown['RIGHT']:
            self.act(self.slot_mouse[1])

        #-- ACT ------------------------------------------------------------------------------#



        #-- HARMS ------------------------------------------------------------------------------#

        # DISORDERS
        if self.disorder_tick['poisoned'] > 0:
            self.damaged(attack.damage(self.disorder_amount['poisoned'], attack.POISON))
            self.disorder_tick['poisoned'] -= 1
        else:
            self.disorder_amount['poisoned'] = 0
        if self.disorder_tick['burning'] > 0:
            self.damaged(attack.damage(self.disorder_amount['burning'], attack.FIRE))
            self.disorder_tick['burning'] -= 1
        else:
            self.disorder_amount['burning'] = 0
        # HARMS
        for h in self.harms:
            self.hp -= h.amount
            self.harms.remove(h)
        if self.hp <= 0:
            self.dead()

        #-- \HARMS ------------------------------------------------------------------------------#
        
    def render(self):
        #pygame.gfxdraw.rectangle(screen, self.poly, WHITE)
        if self.controlled['airborne'] == 0:
            screen.blit(self.image, (self.pos[0] + self.map.cam.offset[0], self.pos[1] + self.map.cam.offset[1]))
        else:
            screen.blit(self.image, (self.pos[0] + self.map.cam.offset[0], self.pos[1] + self.map.cam.offset[1] - 15))

        # DISORDER
        if self.controlled['stunned'] > 0:
            screen.blit(img_stunned, (self.pos[0] + self.map.cam.offset[0], self.pos[1] + self.map.cam.offset[1] - 10))
        if self.controlled['exhaust'] > 0:
            screen.blit(img_exhaust, (self.pos[0] + self.map.cam.offset[0], self.pos[1] + self.map.cam.offset[1] - 10))
        if self.controlled['airborne'] > 0:
            pygame.gfxdraw.filled_ellipse(screen, int(self.pos[0]+self.map.cam.offset[0]+self.ph_stat.width/2), int(self.pos[1]+self.map.cam.offset[1]+self.ph_stat.height-5), 10, 5, (0,0,0,127))
        if self.disorder_tick['poisoned'] > 0:
            screen.blit(img_poisoned, (self.pos[0] + self.map.cam.offset[0], self.pos[1] + self.map.cam.offset[1] - 10))
        if self.disorder_tick['burning'] > 0:
            screen.blit(img_burning, (self.pos[0] + self.map.cam.offset[0], self.pos[1] + self.map.cam.offset[1] - 10))

        # FOOTPRINT: NOT SO COOL, SO NOT USING
        #if self.footprint_tick == 0:
        #    effect.spark_gravity_rectangle((self.pos[0]+self.ph_stat.width/2, self.pos[1]+self.ph_stat.height*2/3), self.footprint_delay*2, (0,1), 3, 5, WHITE, 5)
        #    self.footprint_tick = self.footprint_delay
        #else:
        #    self.footprint_tick -= 1
        
            
            
            
#---------- TEST BENCH ----------#
