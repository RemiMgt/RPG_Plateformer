import pygame
from animation import Animation


class Coffre(Animation):
    def __init__(self, game):
        self.game = game
        super().__init__("coffre", {"coffre": 8}, {"coffre":0.5}, "coffre", is_stop=True, group=self.game.all_coffre)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
