import pygame
from animation import Animation
import random

class Coffre(Animation):
    def __init__(self, game):
        self.game = game
        self.is_loot = False
        super().__init__("coffre", {"coffre": 8}, {"coffre":0.5}, "coffre", is_stop=True, group=self.game.all_coffre)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.old_oui = pygame.image.load("assets/bouton/oui.png")
        self.oui = pygame.image.load("assets/bouton/oui.png")
        self.oui= pygame.transform.scale(self.oui, (self.oui.get_width()//2, self.oui.get_height()//2))
        self.oui_rect = self.oui.get_rect()
        self.oui_rect.x = 490
        self.oui_rect.y =380
        self.old_non = pygame.image.load("assets/bouton/non.png")
        self.non = pygame.image.load("assets/bouton/non.png")
        self.non = pygame.transform.scale(self.non, (self.non.get_width()//2, self.non.get_height()//2))
        self.non_rect = self.non.get_rect()
        self.non_rect.x = 740
        self.non_rect.y =380
        self.fond_gris = pygame.image.load("assets/menu_item.jpg")
        self.fond_gris =pygame.transform.scale(self.fond_gris, (self.fond_gris.get_width()//2, self.fond_gris.get_height()//2))
        self.items = Items()

    def lout(self, screen, background):
        self.animated()
        self.it = self.items.choice_lout()
        if self.it == self.items.armes:
            self.it = self.items.choice_arme()
        else:
            self.it = self.items.choice_potion()
        is_select = self.show(screen, self.it, background)
        if is_select:
            self.game.player.inventaire[0] =self.it

    def show(self, screen, item, background) :
        a = True
        while a:
            mouse = pygame.mouse.get_pos()
            screen.blit(self.fond_gris, (450,200))
            screen.blit(background, (0,0))
            screen.blit(self.oui, self.oui_rect)
            screen.blit(self.non, self.non_rect)
            if self.oui_rect.collidepoint(mouse):
                self.oui= pygame.transform.scale(self.oui, (self.oui.get_width()+10, self.oui.get_height()+10))

            else:
                self.oui= self.old_oui

            if self.non_rect.collidepoint(mouse):
                self.non= pygame.transform.scale(self.non, (self.non.get_width()+10, self.non.get_height()+10))

            else:
                self.non= self.old_non

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    a = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.oui_rect.collidepoint(event.pos):
                        a = False
                        return True
                    if self.non_rect.collidepoint(event.pos):
                        a = False
                        return False

def random_proba(liste, proba):
    chance = random.randrange(0,1)
    for i in range((len(liste)-1)):
        if i == 0:
            if proba[i] < chance:
                return liste[i]
        else:
            if proba[i]+proba[i-1] < chance and proba[i-1]>chance:
                return liste[i]

class Items(Animation) :

    def __init__(self) :
        self.armes = ["epee niveau1", "une super epee niveau 2"]
        self.potions = ["potions de speed de malade", "une potions niveau 2"]
        self.proba_armes=[0.5,0.5]
        self.proba_potions = [0.5,0.5]
        self.proba_lout = [0.3, 0.7]

    def choice_lout(self):
        return random_proba([self.armes, self.potions], self.proba_lout)

    def choice_arme(self):
        return random_proba(self.armes, self.proba_armes)

    def choice_potion(self):
        return random_proba(self.potions, self.proba_potions)
