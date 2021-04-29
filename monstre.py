import pygame
from animation import Animation

class Monstre(Animation) :

    def __init__(self, game) :
        self.game = game
        super().__init__([10], "monstre", ["monstre"], [5], is_stop=False, is_remove=True, group=self.game.all_monstre)
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 80
        self.speed = 6