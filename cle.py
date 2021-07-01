import pygame
from game import *

'''
    1 clé : à ramener dans sortie pour gagner
'''

class Cle :
    def __init__(self, game) :
        self.image = pygame.image.load("assets/cle.png")
        self.rect = self.image.get_rect()
        self.catch = False
        self.game = game

    def put_inventaire(self) :
        pass

    def put_sortie(self) :
        self.game.win = True
