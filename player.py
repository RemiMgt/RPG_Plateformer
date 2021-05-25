import pygame
import random
from animation import Animation  #


class Player(Animation):
    def __init__(self, game):
        super().__init__("player", {"player": 4, "player_run": 8, "player_jump": 6}, {"player": 0.1, "player_run": 0.60, "player_jump": 0.60}, "player", size=(156, 212), is_gauche = True, gauche=[True, True, True])
        self.game = game
        self.movement = [0,0]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speed = 13
        self.speed_jump = -15
        self.health = 5
        self.inventaire = {}
        self.is_jump =False
        self.y_gravite = 1
        self.mouvement = "" #Droite ou Gauche

    def droite(self):
        self.mode = "player_run"
        self.movement[0] = self.speed

    def gauche(self):
        self.mode = "player_run_gauche"
        self.movement[0] = -self.speed

    def saut(self):
        if self.game.air_timer < 12:
            self.movement[1] = self.speed_jump

    def accroupir(self):
        pass
