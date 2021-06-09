import pygame


class Settings:

    def __init__(self):
        self.volume =0
        self.fps =0
        self.load_volume()
        self.load_fps()
        self.touche = {"haut": pygame.K_z, "droite": pygame.K_d, "gauche": pygame.K_q}

        self.font = pygame.font.SysFont(None, 24)
        self.color_text = (255, 255, 255)

        self.text_fps = self.font.render(str(self.fps), True, self.color_text)
        self.text_volume = self.font.render(str(self.volume), True, self.color_text)

        self.fps_text = self.font.render("FPS", True, self.color_text)
        self.volume_text = self.font.render("Volume", True, self.color_text)

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

        # Slider :
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

    def pos_FPS(self):
        self.curseur_FPS.x =self.slider_FPS_image.get_width()*self.fps/120+182
    def pos_volume(self):
        self.curseur_VOLUME.x =self.slider_VOLUME_image.get_width()*self.volume/1+225
    def change_FPS(self):
        self.changing_FPS((int((self.curseur_FPS.x-182)/self.slider_FPS_image.get_width()*120)))
    def change_volume(self):
        self.changing_VOLUME(float(str(((self.curseur_VOLUME.x-182)/self.slider_VOLUME_image.get_width()*1))[:3]))

    def changing_FPS(self, val):
        self.fps = val

    def changing_VOLUME(self, value):
        self.volume = value

    def load_fps(self):
        with open('settings/data_fps.txt') as f:
            ligne = f.readline()[:3]
            self.changing_FPS(int(ligne))

    def extract_fps(self):
        with open('settings/data_fps.txt', 'w') as f:
            f.write(str(self.fps))

    def load_volume(self):
        with open('settings/data_volume.txt') as f :
            ligne = f.readline()[:2]
            self.changing_VOLUME(float(ligne))

    def extract_volume(self):
        with open('settings/data_volume.txt', 'w') as f:
            f.write(str(self.volume))


    def draw(self, window):
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
        window.blit(self.text_fps, (225, 80))
        window.blit(self.text_volume, (225, 280))
        window.blit(self.fps_text, (600, 50))
        window.blit(self.volume_text, (590, 250))

    def generate_rect(self, image, x, y):
        image_rect = image.get_rect()
        image_rect.x = x
        image_rect.y = y
        return image_rect

    def changing(self, selection):
        if selection == "azerty":
            self.touche = {"haut": pygame.K_z, "droite": pygame.K_d, "gauche": pygame.K_q}
            self.selection_azerty = self.bouton_rond_remplie_image
            self.selection_qwerty = self.bouton_rond_vide_image
            self.selection_fleche = self.bouton_rond_vide_image
        elif selection == "qwerty":
            self.touche = {"haut": pygame.K_w, "droite": pygame.K_d, "gauche": pygame.K_a}
            self.selection_azerty = self.bouton_rond_vide_image
            self.selection_qwerty = self.bouton_rond_remplie_image
            self.selection_fleche = self.bouton_rond_vide_image
        else:
            self.touche = {"haut": pygame.K_UP, "droite": pygame.K_RIGHT, "gauche": pygame.K_LEFT}
            self.selection_azerty = self.bouton_rond_vide_image
            self.selection_qwerty = self.bouton_rond_vide_image
            self.selection_fleche = self.bouton_rond_remplie_image
