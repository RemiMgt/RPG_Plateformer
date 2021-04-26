#!/usr/bin/env python3

""" Cahier des charges:

    Principe du jeu:

    personnages:

    modules :
    - numpy (pour les random et autres)
    - pygame_gui eventuellement pour des popups (ajouter des pages)

Elements a dev:
    -physiques
    -gestion des monstres (IA)
    -gestion des niveaux
    -gestion coffres armes et menu
    -gestion du personnage(vie, inventaire, etc)

Options :
    - Musique
    - touches
    - fps


"""


#Importations :
import pygame
import random
from game import Game

#Initialisation :
pygame.init()

#Création fenêtre :
fenetre_width, fenetre_height = 1290, 723
pygame.display.set_caption("Titre jeu")
fenetre = pygame.display.set_mode((fenetre_width, fenetre_height))#, FULLSCREEN

#Menu :
background = pygame.image.load("assets/fond_ecran.jpg")
background = pygame.transform.scale(background, (fenetre_width, fenetre_height))
images_boutons = pygame.image.load("bouton/boutons.png")
gif_menu = pygame.image.load("sprite/idle/perso_idle.gif")
gif_menu = pygame.transform.scale(gif_menu, (900, 900))

#Fonctions :
def generate_in_images(lien, pos, size,surface):
    new_image = images_boutons.subsurface(surface)
    new_image = pygame.transform.scale(new_image, size)
    new_image_rect = new_image.get_rect()
    new_image_rect.x = pos[0]
    new_image_rect.y = pos[1]
    return [new_image, new_image_rect]

def generate_rect(lien, pos) :
    new_image = pygame.image.load(lien)
    new_image_rect = new_image.get_rect()
    new_image_rect.x = pos[0]
    new_image_rect.y = pos[1]
    return [new_image, new_image_rect]

#Boutons :
bouton_play = generate_in_images("bouton/bouton_play.png", (230,150), (300,105), (220, 195, 20, 50))
bouton_settings = generate_in_images("bouton/bouton_option.png", (230,350),(300,105)  ,(220, 135, 150, 50))
bouton_exit = generate_in_images("bouton/bouton_exit.png", (230,550), (300, 105), (42, 20, 244, 90))
bouton_retour = generate_rect("bouton/bouton_retour.png", (30, 690))

#Fonctions :
def menu() :
    fenetre.blit(background, (0, 0))
    fenetre.blit(gif_menu, (700, -40))
    fenetre.blit(bouton_exit[0], bouton_exit[1])
    fenetre.blit(bouton_play[0], bouton_play[1])
    fenetre.blit(bouton_settings[0], bouton_settings[1])

def options():
    fenetre.blit(background, (0, 0))
    fenetre.blit(bouton_retour[0], bouton_retour[1])

def jeux():
    pass

#Création game :
game = Game()

#Boucle principale :
boucle = True
while boucle :

    x, y = pygame.mouse.get_pos()

    # :hover --> boutons :
    if bouton_play[1].collidepoint((x,y)) :
        bouton_play[0] = pygame.transform.scale(bouton_play[0], (320, 120))
        bouton_play[1].x, bouton_play[1].y = 240, 140
    else:
        bouton_play = generate_in_images("bouton/bouton_play.png", (230,150), (300,105), (332, 304, 249, 90))
        bouton_play[1].x, bouton_play[1].y = 250, 150

    if bouton_settings[1].collidepoint((x,y)) :
        bouton_settings[0] = pygame.transform.scale(bouton_settings[0], (320,120))
        bouton_settings[1].x, bouton_settings[1].y = 240, 340
    else:
        bouton_settings = generate_in_images("bouton/bouton_option.png", (230,350),(300,105)  ,(343, 209, 240, 90))
        bouton_settings[1].x, bouton_settings[1].y = 250, 350

    if bouton_exit[1].collidepoint((x,y)) :
        bouton_exit[0] = pygame.transform.scale(bouton_exit[0], (320, 120))
        bouton_exit[1].x, bouton_exit[1].y = 240, 540
    else:
        bouton_exit = generate_in_images("bouton/bouton_exit.png", (230,550), (300, 105), (42, 20, 244, 90))
        bouton_exit[1].x, bouton_exit[1].y = 250, 550

    #Stats :
    if game.stat == "menu":
        menu()
    if game.stat == "options" :
        options()
    if game.stat == "game" :
        jeux()

    pygame.display.flip()

    for event in pygame.event.get() :

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            boucle = False
            print("Closing Project ...")

        if event.type == pygame.KEYDOWN :
            game.keys[event.key] = True

        if event.type == pygame.KEYUP:
            game.keys[event.key] = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            if game.stat == "menu" :
                if bouton_play[1].collidepoint(event.pos):
                    game.stat="game"
                    print("lancement du jeu!")
                elif bouton_settings[1].collidepoint(event.pos):
                    game.stat="options"
                elif bouton_exit[1].collidepoint(event.pos):
                    pygame.quit()
                    boucle = False
                    print("Closing Project ...")
            elif game.stat == "options" :
                if bouton_retour[1].collidepoint(event.pos) :
                    game.stat = "menu"
