from setting import *
import pygame

physicalUI = pygame.image.load("img/UI/physical.png")
weapon01UI = pygame.image.load("img/UI/weapon_slot_01.png")
weapon02UI = pygame.image.load("img/UI/weapon_slot_02.png")
util01UI = pygame.image.load("img/UI/util_slot_01.png")
util02UI = pygame.image.load("img/UI/util_slot_02.png")
util03UI = pygame.image.load("img/UI/util_slot_03.png")
util04UI = pygame.image.load("img/UI/util_slot_04.png")


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