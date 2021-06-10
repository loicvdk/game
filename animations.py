############################
########## IMPORT ##########
############################

import pygame
import random

###########################
########## CLASS ##########
###########################

"""
Define a class that will handle all the animations
"""


class Animation(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()

        self.direction = 'down'  # default
        self.current_image_index = 0

        self.images = animations.get(sprite_name)
        self.image = self.images[self.direction][self.current_image_index]
        self.image.set_colorkey([0, 0, 0])

        self.rect = self.image.get_rect()

    def animate(self):
        """Switch to the next image of the list according to self.direction
        Switching is done randomly in order to make the animation smoother.
        """

        # switch to the next image in the list
        self.current_image_index += random.choices(
            [1, 0],
            cum_weights=[1, 5],
            k=1
        )[0]

        # check the end of the animation
        if self.current_image_index >= len(self.images['down']):
            self.current_image_index = 0

        self.image = self.images[self.direction][self.current_image_index]
        self.image.set_colorkey([0, 0, 0])


#################################
########## LOAD IMAGES ##########
#################################

# Done outside of the class to keep the program performance OK
def load_images_player(sprite_name, row):
    """Load the different sprites relative to player.png and 
    store the result in the animations dictionnary.
    """
    list_images = []
    path = f'assets/{sprite_name}.png'

    for column in range(3):
        image = pygame.Surface([32, 32])
        image.blit(
            pygame.image.load(path),
            (0, 0),
            (column * 32, row * 32, 32, 32)
        )

        list_images.append(image)
    return list_images


def load_images_dragon(sprite_name):
    """Load the different sprites relative to the dino.png and 
    store the result in the animation dict.
    """
    list_images = []
    path = f'assets/{sprite_name}.png'

    for nbr in range(11):
        image = pygame.Surface([24, 24])
        image.blit(
            pygame.image.load(path),
            (0, 0),
            (0, nbr * 24, 24, 24)
        )
        list_images.append(image)
    return list_images


######################################
########## STORE ANIMATIONS ##########
######################################

animations = {
    'player': {
        'down': load_images_player('player', 0),
        'left': load_images_player('player', 1),
        'right': load_images_player('player', 2),
        'up': load_images_player('player', 3)
    },
    'dino': {
        'down': load_images_dragon('dino'),
        'left': load_images_dragon('dino'),
        'right': load_images_dragon('dino'),
        'up': load_images_dragon('dino')
    }
}
