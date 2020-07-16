from setting import *
import pygame, pygame.gfxdraw, numpy
import environment as envi

whole = []

#---------- INFO CONTAINING CLASS ----------#
class basic_stat:
    def __init__(self, acc, jump_power, max_speed, hp):
        self.acc = acc
        self.jump_power = jump_power
        self.max_speed = max_speed
        self.hp = hp

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
        self.acc_ext = [0,0]
        self.b_stat = b_stat
        self.ph_stat = ph_stat
        whole.append(self)


#---------- CHILDREN CLASS: PLAYER ----------#
class player(character):
    def __init__(self, name, pos, b_stat, ph_stat):
        character.__init__(self, name, pos, b_stat, ph_stat)
        self.keyset = {'UP':119, 'LEFT':97, 'DOWN':115, 'RIGHT':100}
        self.keydown = {'UP':False, 'LEFT':False, 'DOWN':False, 'RIGHT':False}
    
    def update(self):
        # SELF ACCELERATION
        accel = [0,0]
        if self.keydown['UP'] == True:
            accel[1] -= self.b_stat.acc
        elif self.keydown['LEFT'] == True:
            accel[0] -= self.b_stat.acc
        elif self.keydown['DOWN'] == True:
            accel[1] += self.b_stat.acc
        elif self.keydown['RIGHT'] == True:
            accel[0] += self.b_stat.acc
        
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
        self.speed[0] += self.acc_ext[0]
        self.speed[1] += self.acc_ext[1]

        # POSITION UPDATE
        for i in range(numpy.abs(self.speed[0])):
            if self.speed[0] > 0:
                self.pos[0] += 1
            else:
                self.pos[0] -= 1
            # CHECK AVAILABILITY HERE
        
        for i in range(numpy.abs(self.speed[1])):
            if self.speed[1] > 0:
                self.pos[1] += 1
            else:
                self.pos[1] -= 1
            # CHECK AVAILABILITY HERE

        # AIR DRAG FORCE
        self.speed[0] = int(self.speed[0] * (1-self.ph_stat.air_drag))
        self.speed[1] = int(self.speed[1] * (1-self.ph_stat.air_drag))

        
    def render(self):
        hitbox = pygame.Rect(int(self.pos[0]-self.ph_stat.width/2), int(self.pos[1]-self.ph_stat.height), self.ph_stat.width, self.ph_stat.height)
        pygame.gfxdraw.rectangle(screen, hitbox, WHITE)
        
            
            
            
#---------- TEST BENCH ----------#
def render():
    screen.fill(BLACK)
    for c in whole:
        c.render()

def update():
    for c in whole:
        c.update()
    
    render()

if __name__ == "__main__":
    
    player_bstat = basic_stat(acc=3, jump_power=10, max_speed=10, hp=100)
    player_phstat = physics_stat(width=30, height=40, air_drag=0.2)
    player = player("1P", (500,400), player_bstat, player_phstat)
    
    clock = pygame.time.Clock()

    done = False
    
    while not done:
        
        clock.tick(30)  # 게임의 화면 투사를 30Hz로 설정

        # 이벤트 입력받기
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == player.keyset['UP']:  # key 'w'
                    player.keydown['UP'] = True
                elif event.key == player.keyset['LEFT']:  # key 'a'
                    player.keydown['LEFT'] = True
                elif event.key == player.keyset['DOWN']:  # key 's'
                    player.keydown['DOWN'] = True
                elif event.key == player.keyset['RIGHT']:  # key 'd'
                    player.keydown['RIGHT'] = True
            if event.type == pygame.KEYUP:
                if event.key == player.keyset['UP']:  # key 'w'
                    player.keydown['UP'] = False
                elif event.key == player.keyset['LEFT']:  # key 'a'
                    player.keydown['LEFT'] = False
                elif event.key == player.keyset['DOWN']:  # key 's'
                    player.keydown['DOWN'] = False
                elif event.key == player.keyset['RIGHT']:  # key 'd'
                    player.keydown['RIGHT'] = False

        update()  # call update funtion

        pygame.display.flip()
            
            
            
            
            