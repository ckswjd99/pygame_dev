from setting import *

def render():
    screen.fill(BLACK)
    for c in ch.whole:
        c.render()
    for g in entity.ground_whole:
        g.render()

def update():
    for c in ch.whole:
        c.update()
    
    render()

if __name__ == "__main__":

    #-- GENERATE BLOCKS ------------------------------------------------------------------------------#
    import entity
    entity.board(entity.map_array_example)

    clock = pygame.time.Clock()

    done = False
    
    while not done:
        
        camera_offset[0] -= (camera_offset[0]+player.pos[0]-500)/5
        camera_offset[1] -= (camera_offset[1]+player.pos[1]-300)/5

        clock.tick(30)  # 게임의 화면 투사를 30Hz로 설정

        #-- EVENT MANIPULATION ------------------------------------------------------------------------------#
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

        #-- UPDATE FUNCTION ------------------------------------------------------------------------------#
        update()  # call update funtion

        pygame.display.flip()
            