############################
########## IMPORT ##########
############################

import pygame
import pyscroll
import pytmx

#########################
########## MAP ##########
#########################


class Map:

    def __init__(self, map_name, screen):
        self.map_name = map_name
        self.tmx_data = pytmx.util_pygame.load_pygame(
            f'assets/{self.map_name}.tmx')
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(
            map_data, screen.get_size())
        map_layer.zoom = 1.5

        # Get collision rectangles
        self.walls = []
        for object in self.tmx_data.objects:
            if object.type == 'collision':
                self.walls.append(pygame.Rect(
                    object.x, object.y, object.width, object.height))

        # Draw calc group
        self.group = pyscroll.PyscrollGroup(
            map_layer=map_layer, default_layer=10)  # 5

        # Define house entrance/exit
        entrance_exit_point = self.tmx_data.get_object_by_name('exit_entrance')
        self.entrance = pygame.Rect(entrance_exit_point.x, entrance_exit_point.y,
                                    entrance_exit_point.width, entrance_exit_point.height)
