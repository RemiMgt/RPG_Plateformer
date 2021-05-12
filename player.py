import pygame
import random
from animation import Animation  #


class Player(Animation):
    def __init__(self):
        super().__init__("player", {"player": 4, "player_run": 8, "player_jump": 6}, {"player": 0.1, "player_run": 0.60, "player_jump": 0.60}, "player", size=(356, 412), is_gauche = True, gauche=[True, True, True])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 13
        self.speed_jump = 10
        self.health = 5
        self.inventaire = {}
        self.is_saut = False
        self.is_jump =False
        self.is_redessendre =False
        self.max_hauteur = 10
        self.parcouru_saut = 0

    def droite(self):
        self.mode = "player_run"
        self.rect.x += self.speed

    def gauche(self):
        self.mode = "player_run_gauche"
        self.rect.x -= self.speed

    def saut(self):
        if self.is_saut:
            if self.parcouru_saut >= self.max_hauteur:
                self.is_saut = False
                self.is_redessendre = True
            else:
                self.rect.y -= self.speed_jump
                self.parcouru_saut += 1
        if self.is_redessendre:
            if self.parcouru_saut == 0:
                self.is_redessendre = False
                self.is_jump = False
            else:
                self.rect.y += self.speed_jump
                self.parcouru_saut -=1

    def accroupir(self):
        pass
