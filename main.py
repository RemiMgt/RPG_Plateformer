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
fenetre_width, fenetre_height = 1500, 800
pygame.display.set_caption("Titre jeu")
fenetre = pygame.display.set_mode((fenetre_width, fenetre_height))#, FULLSCREEN

#Menu :
background = pygame.image.load("assets/fond_ecran.jpg")
images_boutons = pygame.image.load("bouton/boutons.png")

#Fonctions :
def generate(lien, pos, size,surface):
    new_image = images_boutons.subsurface(surface)
    new_image = pygame.transform.scale(new_image, size)
    new_image_rect = new_image.get_rect()
    new_image_rect.x = pos[0]
    new_image_rect.y = pos[1]
    return [new_image, new_image_rect]


#Boutons :
bouton_play = generate("bouton/bouton_play.png", (550,150), (300,100), (220, 195, 150, 50))
bouton_settings = generate("bouton/bouton_option.png", (550,350),(300,100)  ,(220, 135, 150, 50))
bouton_exit = generate("bouton/bouton_exit.png", (550,550), (300, 100), (30, 15, 150, 50))
bouton_retour = generate("bouton/bouton_retour.png", (20, 780), (300, 100), (30, 15, 150, 50))

#Fonctions :
def menu() :
    fenetre.blit(background, (0, 0))
    fenetre.blit(bouton_exit[0], (bouton_exit[1]))
    fenetre.blit(bouton_play[0], bouton_play[1])
    fenetre.blit(bouton_settings[0], bouton_settings[1])

def options():
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
        bouton_play[1].x, bouton_play[1].y = 540, 140
    else:
        bouton_play = generate("bouton/bouton_play.png", (550,150), (300,100), (220, 195, 150, 50))
        bouton_play[1].x, bouton_play[1].y = 550, 150

    if bouton_settings[1].collidepoint((x,y)) :
        bouton_settings[0] = pygame.transform.scale(bouton_settings[0], (320,120))
        bouton_settings[1].x, bouton_settings[1].y = 540, 340
    else:
        bouton_settings = generate("bouton/bouton_option.png", (550,350),(300,100)  ,(220, 135, 150, 50))
        bouton_settings[1].x, bouton_settings[1].y = 550, 350

    if bouton_exit[1].collidepoint((x,y)) :
        bouton_exit[0] = pygame.transform.scale(bouton_exit[0], (320, 120))
        bouton_exit[1].x, bouton_exit[1].y = 540, 540
    else:
        bouton_exit =  generate("bouton/bouton_exit.png", (550,550), (300, 100), (30, 15, 150, 50))
        bouton_exit[1].x, bouton_exit[1].y = 550, 550

    if bouton_retour[1].collidepoint((x,y)) :
        bouton_retour[0] = pygame.transform.scale(bouton_retour[0], (320, 120))
        bouton_retour[1].x, bouton_retour[1].y = 540, 540
    else:
        bouton_retour = generate("bouton/bouton_retour.png", (20, 780), (300, 100), (30, 15, 150, 50))
        bouton_retour[1].x, bouton_retour[1].y = 550, 550
        #a demain pylou

    #Stats :
    if game.stat == "menu":
        menu()
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
            if bouton_play[1].collidepoint(event.pos):
                game.stat="game"
                print("lancement du jeu!")
            elif bouton_settings[1].collidepoint(event.pos):
                game.stat="options"
                print("voila les options")
            elif bouton_exit[1].collidepoint(event.pos):
                pygame.quit()
                boucle = False
                print("Closing Project ...")
