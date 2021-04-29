import pygame
import random
from animation import Animation  #


class Player(Animation):
    def __init__(self):
        super().__init__("player", {"player": 4, "player_run": 8, "player_jump": 6}, 0.60, "player", size=(356, 412))
        self.rect = self.image.get_rect()
        self.rect.x = 770
        self.rect.y = 115
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
