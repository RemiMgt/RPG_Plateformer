import pygame
from animation import Animation
import numpy


class Coffre(Animation):
    def __init__(self, game):
        self.game = game
        super().__init__("coffre", {"coffre": 8}, {"coffre":0.5}, "coffre", is_stop=True, group=self.game.all_coffre)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.items = Items()

    def lout(self):
        self.animated()
        self.it = self.items.choice_lout()
        if self.it == self.items.armes:
            self.it = self.items.choice_arme()
        else:
            self.it = self.items.choice_potion()
        self.game.player.inventaire


class Items(Animation) :

    def __init__(self) :
        self.armes = []
        self.potions = []
        self.proba_armes=[]
        self.proba_potions = []
        self.proba_lout = [0.3, 0.7]

    def choice_lout(self):
        return numpy.random.choice([self.armes, self.potions], p=self.proba_lout)

    def choice_arme(self):
        return numpy.random.choice(self.armes, p=self.proba_armes)

    def choice_potion(self):
        return numpy.random.choice(self.potions, p=self.proba_potions)
