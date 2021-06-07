############################
########## IMPORT ##########
############################

import pygame
from player import Player

#############################
########## DRAGONS ##########
#############################


class Dragon(Player):

    def __init__(self, x, y, sprite_name):
        super().init(x, y, sprite_name)

    def spawn(self):
        pass

    def attack(self):
        pass

    def move(self):
        pass
