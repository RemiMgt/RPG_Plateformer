import pygame
import random
from animation import Animation


class Player(Animation):
    def __init__(self):
        super().__init__([4, 8, 6],"player",["player", "player_run", "player_jump"], [15, 4, 6])
        self.rect = self.image.get_rect()
        self.rect.x = 740
        self.rect.y = 80
        self.speed = 7
        self.health = 5
        self.inventaire = {}

    def droite(self):
        #Si pas de collison avec obstacles :
        self.rect.x += self.speed

    def gauche(self):
        #Si pas de collison avec murs :
        self.rect.x -= self.speed

    def saut(self):
        #Si pas de collison avec murs :
        pass

    def accroupir(self):
        pass
