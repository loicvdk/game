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

        self.speed = 1.5
        self.position = [x, y]
        self.previous_position = self.position.copy()
        self.feet_position = pygame.Rect(
            0, 0, self.rect.width / 2, 12)     # abritrary values

    def save_position(self):
        """Set the self.previous position attribute = to the actual position"""
        self.previous_position = self.position.copy()

    # Maybe refactor this with return statement

    def move_right(self):
        self.direction = 'right'
        self.position[0] += self.speed
        self.animate()

    def move_left(self):
        self.direction = 'left'
        self.position[0] -= self.speed
        self.animate()

    def move_up(self):
        self.direction = 'up'
        self.position[1] -= self.speed
        self.animate()

    def move_down(self):
        self.direction = 'down'
        self.position[1] += self.speed
        self.animate()

    def update(self):
        # Change position to the rectangle which position the player
        self.rect.topleft = self.position
        self.feet_position.midbottom = self.rect.midbottom

    def move_back(self):
        """If player enter in collision, retake the previous position"""
        self.position = self.previous_position
        self.update()

    def spawn(self, tmx):
        # should be replace by (f'spawn_{sprite_anme}') like that I could inheretate this method for the dragons
        spawn_point = tmx.get_object_by_name('spawn')
        self.position = [spawn_point.x, spawn_point.y - 20]
