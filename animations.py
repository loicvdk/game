############################
########## IMPORT ##########
############################

import pygame


###########################
########## CLASS ##########
###########################

"""
Define a class that will handle all the animations
"""


class Animation(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()

        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.list_images = []


#################################
########## LOAD IMAGES ##########
#################################
def load_images(sprite_name):
    pass


######################################
########## STORE ANIMATIONS ##########
######################################
animations = {
    'player': {
        'down': [],
        'left': [],
        'right': [],
        'up': []
    }
}
