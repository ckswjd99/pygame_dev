from setting import *
import pygame



#-- PRIMITIVE CLASS: UI ------------------------------------------------------------------------------#
class UI:
    def __init__(self, map):
        self.map = map
        self.physicalUI = pygame.image.load("img/UI/physical.png")
        self.hp_bar = pygame.image.load("img/UI/hp_bar.png")
        self.mp_bar = pygame.image.load("img/UI/mp_bar.png")
        self.weapon01UI = pygame.image.load("img/UI/weapon_slot_01.png")
        self.weapon02UI = pygame.image.load("img/UI/weapon_slot_02.png")
        self.util01UI = pygame.image.load("img/UI/util_slot_01.png")
        self.util02UI = pygame.image.load("img/UI/util_slot_02.png")
        self.util03UI = pygame.image.load("img/UI/util_slot_03.png")
        self.util04UI = pygame.image.load("img/UI/util_slot_04.png")
    
    def update(self):
        # HP, MP bar
        self.physicalUI = pygame.image.load("img/UI/physical.png")
        self.physicalUI.blit(self.hp_bar, (42,8), pygame.Rect((0,0), (int(self.hp_bar.get_width()*self.map.player.hp/self.map.player.b_stat.max_hp),self.hp_bar.get_height())))
        self.physicalUI.blit(self.mp_bar, (42,32), pygame.Rect((0,0), (int(self.mp_bar.get_width()*self.map.player.mp/self.map.player.b_stat.max_mp),self.mp_bar.get_height())))


    def render(self):
            screen.blit(self.physicalUI, (size[0]/2-self.physicalUI.get_width()/2, size[1]-self.physicalUI.get_height()-10))
            screen.blit(self.weapon01UI, (size[0]-self.weapon01UI.get_width()*2-20, size[1]-self.weapon01UI.get_height()-10))
            screen.blit(self.weapon02UI, (size[0]-self.weapon02UI.get_width()-10, size[1]-self.weapon02UI.get_height()-10))
            screen.blit(self.util01UI, (10, size[1]-self.util01UI.get_height()-10))
            screen.blit(self.util02UI, (10+self.util02UI.get_width()+10, size[1]-self.util02UI.get_height()-10))
            screen.blit(self.util03UI, (10+(self.util03UI.get_width()+10)*2, size[1]-self.util03UI.get_height()-10))
            screen.blit(self.util04UI, (10+(self.util04UI.get_width()+10)*3, size[1]-self.util04UI.get_height()-10))



def update():

    pass

def render():
    screen.blit(physicalUI, (size[0]/2-physicalUI.get_width()/2, size[1]-physicalUI.get_height()-10))
    screen.blit(weapon01UI, (size[0]-weapon01UI.get_width()*2-20, size[1]-weapon01UI.get_height()-10))
    screen.blit(weapon02UI, (size[0]-weapon02UI.get_width()-10, size[1]-weapon02UI.get_height()-10))
    screen.blit(util01UI, (10, size[1]-util01UI.get_height()-10))
    screen.blit(util02UI, (10+util02UI.get_width()+10, size[1]-util02UI.get_height()-10))
    screen.blit(util03UI, (10+(util03UI.get_width()+10)*2, size[1]-util03UI.get_height()-10))
    screen.blit(util04UI, (10+(util04UI.get_width()+10)*3, size[1]-util04UI.get_height()-10))

#-- TEST BENCH ------------------------------------------------------------------------------#
if __name__ == "__main__":
    pass