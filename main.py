############################
########## IMPORT ##########
############################

from game import Game
import pygame


##########################
########## MAIN ##########
##########################

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.run()
