import pygame
import random

class Player(pygame.sprite.Sprite) :
    def __init__(self) :
        self.image = pygame.image.load("sprite/perso.png")
        self.rect = self.image.get_rect()
        self.speed = 7
        self.health = 5
        self.inventaire = {}

    def droite(self) :
        #Si pas de collison avec murs :
        self.rect.x += self.speed

    def gauche(self) :
        #Si pas de collison avec murs :
        self.rect.x -= self.speed

    def saut(self) :
        #Si pas de collison avec murs :
        pass

    def accroupir(self) :
        pass
