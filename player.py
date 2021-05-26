############################
########## IMPORT ##########
############################

import pygame

############################
########## PLAYER ##########
############################


class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.sprite_sheet = pygame.image.load('assets/player.png')
        self.position = [x, y]
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

    def change_image(self, direction):
        self.image = self.images[direction]
        self.image.set_colorkey([0, 0, 0])

    # Maybe refactor this

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

    def get_image(self, x, y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image