import pygame
from player import Player

class Game :
    def __init__(self):
        self.keys ={}
        self.player = Player()
        self.stat = "menu"
        self.index = 0

    def check_collision(self, sprite, group): #FOnction qui retrun True si il y a collision entre sprite et group
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask) #sprite / group / Oui ou non détruire entité si il y a collision

    def check_collision_sprite(self, rect1, rect2): #FOnction qui retrun True si il y a collision entre sprite et group
        return pygame.sprite.collide_rect(rect1, rect2) #sprite / group / Oui ou non détruire entité si il y a collision
