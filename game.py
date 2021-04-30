import pygame
from player import Player
from coffre import Coffre
from monstre import Monstre
from map import *
from setting import Settings


class Game :
    def __init__(self):
        self.keys = {}
        self.all_coffre = pygame.sprite.Group()
        self.all_monstre = pygame.sprite.Group()
        self.all_coffre.add(Coffre(self))
        self.all_monstre.add(Monstre(self))
        self.player = Player()
        self.stat = "menu"
        self.index = 0
        self.setting = Settings()

    def check_collision(self, sprite, group): #FOnction qui retrun True si il y a collision entre sprite et group
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask) #sprite / group / Oui ou non détruire entité si il y a collision

    def check_collision_sprite(self, rect1, rect2): #FOnction qui retrun True si il y a collision entre sprite et group
        return pygame.sprite.collide_rect(rect1, rect2) #sprite / group / Oui ou non détruire entité si il y a collision
