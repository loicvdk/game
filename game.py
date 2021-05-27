############################
########## IMPORT ##########
############################

import pygame
import pytmx
import pyscroll
from player import Player
from maps import Map

##########################
########## GAME ##########
##########################


class Game:

    def __init__(self):
        # Create window
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('My Game')

        self.map = Map('world', self.screen)

        # Generate player
        player_initial_position = self.map.tmx_data.get_object_by_name(
            'initial_position')
        self.player = Player(player_initial_position.x,
                             player_initial_position.y)

        self.map.group.add(self.player)

    def handle_input(self):
        pressed_key = pygame.key.get_pressed()

        if pressed_key[pygame.K_UP] or pressed_key[pygame.K_z]:
            self.player.move_up()
        elif pressed_key[pygame.K_DOWN] or pressed_key[pygame.K_s]:
            self.player.move_down()
        elif pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]:
            self.player.move_right()
        elif pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_q]:
            self.player.move_left()

    def switch_map(self, map_name):
        self.map = Map(map_name, self.screen)

    def update(self):
        self.map.group.update()

        # Check house entrance
        if self.player.feet_position.colliderect(self.map.entrance):
            if self.map.map_name == 'world':
                self.switch_map('house')
            elif self.map.map_name == 'house':
                self.switch_map('world')
            self.map.group.add(self.player)
            self.player.spawn(self.map.tmx_data)

        # Check collisions
        for sprite in self.map.group.sprites():
            if sprite.feet_position.collidelist(self.map.walls) > -1:
                sprite.move_back()

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:

            self.player.save_position()
            self.handle_input()
            self.update()
            self.map.group.center(self.player.rect.center)
            self.map.group.draw(self.screen)
            pygame.display.flip()  # To reload everything eachtime

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick(60)      # Set FPS to 60/sec

    pygame.quit()
