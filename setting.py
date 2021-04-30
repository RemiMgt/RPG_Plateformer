import pygame

class Settings:

    def __init__(self) :
        self.volume = 0.1
        self.fps =60
        self.touche = {"selection": "azerty", "haut" : pygame.K_UP, "droite" : pygame.K_RIGHT, "gauche" : pygame.K_LEFT}

        self.bouton_rond_remplie = pygame.image.load("assets/bouton/bouton_settings_remplie.png")
        self.bouton_rond_vide = pygame.image.load("assets/bouton/bouton_settings_vide.png")
        self.b_touche_azerty = pygame.image.load('assets/bouton/azerty.png')
        self.b_touche_qwerty = pygame.image.load('assets/bouton/qwerty.png')
        self.b_touche_fleche = pygame.image.load('assets/bouton/fleche.png')

        self.b_touche_azerty = self.scale(self.b_touche_azerty, 200, 100)
        self.b_touche_qwerty = self.scale(self.b_touche_qwerty, 200, 100)
        self.b_touche_fleche = self.scale(self.b_touche_fleche, 200, 100)

        if self.touche["selection"] == "azerty":

            self.selection_azerty = self.bouton_rond_remplie
            self.selection_qwerty = self.bouton_rond_vide
            self.selection_fleche = self.bouton_rond_vide

        elif self.touche["selection"] == "qwerty":

            self.selection_azerty = self.bouton_vide
            self.selection_fleche = self.bouton_rond_vide
            self.selection_qwerty = self.bouton_rond_remplie

        else:
            self.selection_azerty = self.bouton_vide
            self.selection_qwerty = self.bouton_vide
            self.selection_fleche = self.bouton_rond_remplie



    def changing_FPS(self, val) :
        self.fps = val


    def changing_VOLUME(self, value) :
        self.volume = val


    def draw(self, window) :
        window.blit(self.selection_azerty,(100,100))
        window.blit(self.selection_qwerty,(100, 300))
        window.blit(self.selection_fleche,(100, 300))
        window.blit(self.b_touche_fleche, (400, 100))
        window.blit(self.b_touche_qwerty, (400, 300))
        window.blit(self.b_touche_azerty, (400, 500))

    def scale(self, item, width, height) :
        return pygame.transform.scale(item, (width, height))
