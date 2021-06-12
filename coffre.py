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
        self.oui = pygame.image.load("assets/bouton/oui.png")
        self.oui_rect = self.oui.get_rect()
        self.non = pygame.image.load("assets/bouton/non.png")
        self.non_rect = self.non.get_rect()
        self.fond_gris = pygame.image.load("assets/menu_item.jpg")
        self.items = Items()

    def lout(self, screen, background):
        self.animated()
        self.it = self.items.choice_lout()
        if self.it == self.items.armes:
            self.it = self.items.choice_arme()
        else:
            self.it = self.items.choice_potion()
        is_select = self.show(screen, self.it)
        if is_select:
            self.game.player.inventaire[0] =self.it

    def show(self, screen, item, background) :
        a = True
        while a:
            screen.blit(background, (0,0))
            screen.blit(self.fond_gris, (200,200))
            screen.blit(self.oui, self.oui_rect)
            screen.blit(self.non, self.non_rect)
            pygame.display.flip()
            for event in pygame.get_event():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if oui_rect.collidepoint(event.pos):
                        a = False
                        return True
                    if non_rect.collidepoint(event.pos):
                        a = False
                        return False

class Items(Animation) :

    def __init__(self) :
        self.armes = ["epee niveau1", "une super epee niveau 2"]
        self.potions = ["potions de speed de malade", "une potions niveau 2"]
        self.proba_armes=[0.5,0.5]
        self.proba_potions = [0.5,0.5]
        self.proba_lout = [0.3, 0.7]

    def choice_lout(self):
        return numpy.random.choice([self.armes, self.potions], p=self.proba_lout)

    def choice_arme(self):
        return numpy.random.choice(self.armes, p=self.proba_armes)

    def choice_potion(self):
        return numpy.random.choice(self.potions, p=self.proba_potions)
