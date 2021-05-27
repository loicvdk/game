############################
########## IMPORT ##########
############################

import pygame
from animations import Animation

############################
########## PLAYER ##########
############################


class Player(Animation):

    def __init__(self, x, y, sprite_name):
        super().__init__(sprite_name)

        self.sprite_sheet = pygame.image.load('assets/player.png')
        self.speed = 3
        self.image = self.get_image(0, 0)
        self.image.set_colorkey([0, 0, 0])
        # ?? lorsqu'on definit une image on doit définir un rectange pour le placer
        self.rect = self.image.get_rect()
        self.images = {
            'down': self.get_image(0, 0),
            'left': self.get_image(0, 32),
            'right': self.get_image(0, 64),
            'up': self.get_image(0, 96)
        }
        self.position = [x, y]
        self.previous_position = self.position.copy()
        self.feet_position = pygame.Rect(
            0, 0, self.rect.width / 2, 12)     # abritrary values

    def save_position(self):
        """Set the self.previous position attribute = to the actual position"""
        self.previous_position = self.position.copy()

    def change_image(self, direction):
        """Set the corresponding image according to the direction pressed"""
        self.image = self.images[direction]
        self.image.set_colorkey([0, 0, 0])

    # Maybe refactor this with return statement

    def move_right(self):
        self.change_image('right')
        self.position[0] += self.speed

    def move_left(self):
        self.change_image('left')
        self.position[0] -= self.speed

    def move_up(self):
        self.change_image('up')
        self.position[1] -= self.speed

    def move_down(self):
        self.change_image('down')
        self.position[1] += self.speed

    def update(self):
        # Change position to the rectangle which position the player
        self.rect.topleft = self.position
        self.feet_position.midbottom = self.rect.midbottom

    def move_back(self):
        """If player enter in collision, retake the previous position"""
        self.position = self.previous_position
        self.update()

    def spawn(self, tmx):
        spawn_point = tmx.get_object_by_name('spawn')
        self.position = [spawn_point.x, spawn_point.y - 20]

    def get_image(self, x, y):
        """Return the image wanted given a x and y position that should refer to the player.png file"""
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image
