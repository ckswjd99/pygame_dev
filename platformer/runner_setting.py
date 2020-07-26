############################## README ############################################################
##  This file generates objects in use.
## 
##  This file generates maps.
##  Every maps generated are stored in dictionary type 'maps'.
##  
##################################################################################################

import mapping
import entity
import attack
from runner import *


#-- GENERATE PLAYER ------------------------------------------------------------------------------#
import character as ch
player_bstat = ch.basic_stat(acc=3, jump_power=10, max_speed=10, max_hp=100, max_mp=100)
player_phstat = ch.physics_stat(width=20, height=20, air_drag=0.2)
player = ch.player("1P", (500,400), player_bstat, player_phstat)


#-- MAPS FOR USE ------------------------------------------------------------------------------#
maps = {}

# TEST MAP (test_map)
test_map = mapping.mapping((40, 24))
test_map_chars = []
temp = ch.character("HEOSU", (600, 300), player_bstat, player_phstat)
temp.set_map(test_map)
test_map_chars.append( temp )

test_map.map_setting(mapping.map_temp, {'start': (50,300)}, test_map_chars)
test_map.background_setting(pygame.image.load("img/map/test_map_bg.png"))
test_map.add_block( entity.eventblock(test_map, (5,5), entity.PLAYER_COLLIDE, lambda: test_map.player.harms.append(attack.damage(5, False))) )
test_map.add_block( entity.eventblock(test_map, (10,5), entity.PLAYER_COLLIDE, lambda: test_map.player.set_acc((3,3), 10)) )
test_map.add_block( entity.eventblock(test_map, (15,5), entity.PLAYER_COLLIDE, lambda: test_map.player.set_controlled('stunned', 30)) )
test_map.add_block( entity.eventblock(test_map, (20,5), entity.PLAYER_COLLIDE, lambda: test_map.player.set_controlled('exhaust', 30)) )
test_map.add_block( entity.eventblock(test_map, (25,5), entity.PLAYER_COLLIDE, lambda: test_map.player.set_controlled('airborne', 10)) )
test_map.add_block( entity.eventblock(test_map, (30,5), entity.PLAYER_COLLIDE, lambda: test_map.player.set_disorder('poisoned', 30, 1)) )
test_map.add_block( entity.eventblock(test_map, (35,5), entity.PLAYER_COLLIDE, lambda: test_map.player.set_disorder('burning', 300, 0.1)) )
test_map.carpets.append( attack.carpet( (250,500), pygame.Rect(250,500,50,50), attack.damage(1, attack.NORMAL), 2, player, [] ) )
maps['test_map'] = test_map

# TEST MAP 2 (test_map2)
test_map2 = mapping.mapping((30,20))
test_map2.map_setting([], {'start': (450,250)}, [])
test_map2.background_setting(pygame.image.load("img/map/test_map2_bg.png"))
test_map2.add_block( entity.portalblock(test_map2, (15,5), to_map=maps['test_map'], to_pos=maps['test_map'].spawn_list['start']) )
maps['test_map2'] = test_map2

# START MAP (start_map)
start_map = mapping.mapping((100,15))
start_map.map_setting([], {'start': (200,110)}, [])
start_map.background_setting(pygame.image.load("img/map/start_map_bg.png"))

maps['start_map'] = start_map