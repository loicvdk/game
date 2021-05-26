############################
########## IMPORT ##########
############################

import pygame
import pytmx
import pyscroll
from player import Player

##########################
########## GAME ##########
##########################


class Game:

    def __init__(self):
        # Create window
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('My Game')

        # Load map
        tmx_data = pytmx.util_pygame.load_pygame('assets/map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, self.screen.get_size())
        map_layer.zoom = 2

        # Generate player
        player_initial_position = tmx_data.get_object_by_name(
            'initial_position')
        self.player = Player(player_initial_position.x,
                             player_initial_position.y)

        # Draw calc group   (give map data, default = default_layer in order to not have the player behind the water etc.)
        self.group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=3)

        self.group.add(self.player)

    def handle_input(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_UP]:
            self.player.move_up()
        elif pressed_key[pygame.K_DOWN]:
            self.player.move_down()
        elif pressed_key[pygame.K_RIGHT]:
            self.player.move_right()
        elif pressed_key[pygame.K_LEFT]:
            self.player.move_left()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:

            self.handle_input()
            self.group.update()
            self.group.center(self.player.rect.center)
            self.group.draw(self.screen)
            pygame.display.flip()  # To reload everything eachtime

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)      # Set FPS to 60/sec

    pygame.quit()
