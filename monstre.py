import pygame
from animation import Animation


class Monstre(Animation) :

    def __init__(self, game, type) :
        """
            Type : Basique / Medium / Colossal
        """
        self.game = game
        super().__init__("monstre", {"monstre": 10}, {"monstre":0.5}, "monstre", is_stop=True, group=self.game.all_monstre)
        self.rect = self.image.get_rect()
        self.rect.x = 700
        self.rect.y = 80
        self.speed = 6
        self.tab_health = {"basique" : 3, "medium" : 5, "colossal" : 10}
        self.health = self.tab_health[type]
        self.tab_damage = {"basique" : 1, "medium" : 2, "colossal" : 3}

    def show(self,window, pos) :
        window.blit(self.image, self.rect)

    def damage(self, degat, arme) :
        self.game.player.health -= self.tab_damage[arme]

    def move(self, layer0):
        #if layer0[][] !=0

        pass
