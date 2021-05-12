import pygame

class Settings:

    def __init__(self) :
        self.volume = 0.1
        self.fps = 60
        self.touche = {"haut" : pygame.K_SPACE, "droite" : pygame.K_d, "gauche" : pygame.K_q}

        self.bouton_rond_remplie_image = pygame.image.load("assets/bouton/bouton_settings_remplie.png")
        self.bouton_rond_vide_image = pygame.image.load("assets/bouton/bouton_settings_vide.png")

        self.b_touche_azerty = pygame.image.load('assets/bouton/azerty.png')
        self.b_touche_qwerty = pygame.image.load('assets/bouton/qwerty.png')
        self.b_touche_fleche = pygame.image.load('assets/bouton/fleche.png')

        self.b_touche_azerty = pygame.transform.scale(self.b_touche_azerty, (200, 100))
        self.b_touche_qwerty = pygame.transform.scale(self.b_touche_qwerty, (200, 100))
        self.b_touche_fleche = pygame.transform.scale(self.b_touche_fleche, (200, 100))

        self.selection_azerty = self.bouton_rond_remplie_image
        self.selection_qwerty = self.bouton_rond_vide_image
        self.selection_fleche = self.bouton_rond_vide_image

        self.selection_azerty_rect = self.generate_rect(self.selection_azerty, 880, 650)
        self.selection_qwerty_rect = self.generate_rect(self.selection_qwerty, 580, 650)
        self.selection_fleche_rect = self.generate_rect(self.selection_fleche, 280, 650)

        #Slider :
        self.slider_FPS_image = pygame.image.load("assets/settings/slider.png")
        self.slider_VOLUME_image = pygame.image.load("assets/settings/slider.png")
        self.curseur_image_FPS = pygame.image.load("assets/settings/curseur.png")
        self.curseur_image_VOLUME = pygame.image.load("assets/settings/curseur.png")

        self.curseur_image_VOLUME = pygame.transform.scale(self.curseur_image_VOLUME, (40, 40))
        self.curseur_image_FPS = pygame.transform.scale(self.curseur_image_FPS, (40, 40))

        self.slider_FPS = self.generate_rect(self.slider_FPS_image, 220, 100)
        self.slider_VOLUME = self.generate_rect(self.slider_VOLUME_image, 220, 300)
        self.curseur_FPS = self.generate_rect(self.curseur_image_FPS, 620, 100)
        self.curseur_VOLUME = self.generate_rect(self.curseur_image_VOLUME, 620, 300)


    def changing_FPS(self, val) :
        self.fps = val


    def changing_VOLUME(self, value) :
        self.volume = val


    def draw(self, window) :
        window.blit(self.selection_azerty, self.selection_azerty_rect)
        window.blit(self.selection_qwerty, self.selection_qwerty_rect)
        window.blit(self.selection_fleche, self.selection_fleche_rect)
        window.blit(self.slider_FPS_image, self.slider_FPS)
        window.blit(self.slider_VOLUME_image, self.slider_VOLUME)
        window.blit(self.curseur_image_FPS, self.curseur_FPS)
        window.blit(self.curseur_image_VOLUME, self.curseur_VOLUME)
        window.blit(self.b_touche_fleche, (200, 500))
        window.blit(self.b_touche_qwerty, (500, 500))
        window.blit(self.b_touche_azerty, (800, 500))

    def generate_rect(self, image, x, y) :
        image_rect = image.get_rect()
        image_rect.x = x
        image_rect.y = y
        return image_rect

    def changing(self, selection) :
        if selection == "azerty" :
            self.touche = {"haut" : pygame.K_z, "droite" : pygame.K_d, "gauche" : pygame.K_q}
            self.selection_azerty = self.bouton_rond_remplie_image
            self.selection_qwerty = self.bouton_rond_vide_image
            self.selection_fleche = self.bouton_rond_vide_image
        elif selection == "qwerty" :
            self.touche = {"haut" : pygame.K_w, "droite" : pygame.K_d, "gauche" : pygame.K_a}
            self.selection_azerty = self.bouton_rond_vide_image
            self.selection_qwerty = self.bouton_rond_remplie_image
            self.selection_fleche = self.bouton_rond_vide_image
        else :
            self.touche = {"haut" : pygame.K_UP, "droite" : pygame.K_RIGHT, "gauche" : pygame.K_LEFT}
            self.selection_azerty = self.bouton_rond_vide_image
            self.selection_qwerty = self.bouton_rond_vide_image
            self.selection_fleche = self.bouton_rond_remplie_image
