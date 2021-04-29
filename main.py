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

Fond ecran :
    - Fond ecran : fond ecran de la map flouté


"""


#Importations :
import pygame
import time
from random import *
from pygame.locals import *

from game import Game
from animation import Animation
from map import *

#Initialisation :
pygame.init()

#FPS :
FPS = 60
fpsClock = pygame.time.Clock()

#Music :
musique_menu = pygame.mixer.Sound("assets/music/musique_accueil.ogg")
musique_menu.set_volume(0.1)
musique_menu.play(-1)

#Bruitages :
bruitage_avancer = pygame.mixer.Sound("assets/music/bruitage_avancer.ogg")
bruitage_reculer = pygame.mixer.Sound("assets/music/bruitage_retour.ogg")
bruitage_avancer.set_volume(5)
bruitage_reculer.set_volume(5)

#Création fenêtre :
fenetre_width, fenetre_height = 1290, 723  #1290 / 723
pygame.display.set_caption("Titre jeu")
fenetre = pygame.display.set_mode((fenetre_width, fenetre_height))

#Menu :
background = pygame.image.load("assets/fond_ecran.png")
background = pygame.transform.scale(background, (fenetre_width, fenetre_height))
images_boutons = pygame.image.load("assets/bouton/boutons.png")

#Fonctions :

def generate_rect(lien, pos) :
    new_image = pygame.image.load(lien)
    new_image_rect = new_image.get_rect()
    new_image_rect.x = pos[0]
    new_image_rect.y = pos[1]
    return [new_image, new_image_rect]

def gravite(image_rect, rayon, coord_centre, vitesse) :
    nb_random = randint(1, 4)
    if nb_random == 1 and image_rect.y - vitesse >= coord_centre[1] - rayon : #Haut
        image_rect.y -= vitesse
    elif nb_random == 2 and image_rect.y + vitesse <= coord_centre[1] + rayon : #Bas
        image_rect.y += vitesse
    elif nb_random == 3 and image_rect.x + vitesse <= coord_centre[0] + rayon : #Droite
        image_rect.x += vitesse
    elif nb_random == 4 and image_rect.x - vitesse >= coord_centre[0] - rayon : #Gauche
        image_rect.x -= vitesse

def generate_rect_button(lien, pos, dim) :
    new_image = pygame.image.load(lien)
    new_image = pygame.transform.scale(new_image, (dim[0], dim[1]))
    new_image_rect = new_image.get_rect()
    new_image_rect.x = pos[0]
    new_image_rect.y = pos[1]
    return [new_image, new_image_rect]


#Boutons :
bouton_play = generate_rect_button("assets/bouton/bouton_play.png", (250, 150), (170, 45))
bouton_settings = generate_rect_button("assets/bouton/bouton_option.png", (250, 350), (170, 45))
bouton_exit = generate_rect_button("assets/bouton/bouton_exit.png", (250, 550), (170, 45))
bouton_retour = generate_rect_button("assets/bouton/bouton_retour.png", (30, 650), (170, 45))

#Gravité :
socle = generate_rect("assets/support.png", (750, 570))
socle[0] = pygame.transform.scale(socle[0], (400, 100))
delay = 5
tab_gravite = ["False"] * delay
tab_gravite.append("True")

index_gravite = 0

#Map :
map = Map(64, 64)

map.map_import("map")

#Fonctions jeux:
def menu() :
    fenetre.blit(background, (0, 0))
    fenetre.blit(bouton_exit[0], bouton_exit[1])
    fenetre.blit(bouton_play[0], bouton_play[1])
    fenetre.blit(bouton_settings[0], bouton_settings[1])

def options():
    fenetre.blit(background, (0, 0))
    fenetre.blit(bouton_retour[0], bouton_retour[1])

def jeux():
    fenetre.blit(background, (0, 0))
    for x in range(len(map.blockmaplayer0)):
        for y in range(len(map.blockmaplayer0[x])):
            fenetre.blit(blocks.blockstextures[map.blockmaplayer0[x][y]], (x*48, y*48))
    for x in range(len(map.blockmaplayer1)):
        for y in range(len(map.blockmaplayer1[x])):
            fenetre.blit(blocks.blockstextures[map.blockmaplayer1[x][y]], (x*48, y*48))
    fenetre.blit(bouton_retour[0], bouton_retour[1])
    for coffre in game.all_coffre:
        fenetre.blit(coffre.image, coffre.rect)
        coffre.animated(0)
    for monstre in game.all_monstre :
        fenetre.blit(monstre.image, monstre.rect)
        monstre.animated(0)

#Création game :
game = Game()

#Boucle principale :
boucle = True
while boucle :

    #FPS :
    fpsClock.tick(FPS)
    pygame.display.update()

    #Mouse :
    x, y = pygame.mouse.get_pos()

    # :hover --> boutons :
    if bouton_play[1].collidepoint((x,y)) :
        bouton_play = generate_rect_button("assets/bouton/bouton_play.png", (245, 245), (180, 55))
    else:
        bouton_play = generate_rect_button("assets/bouton/bouton_play.png", (250, 250), (170, 45))

    if bouton_settings[1].collidepoint((x,y)) :
        bouton_settings = generate_rect_button("assets/bouton/bouton_option.png", (145, 345), (180, 55))
    else:
        bouton_settings = generate_rect_button("assets/bouton/bouton_option.png", (150, 350), (170, 45))

    if bouton_exit[1].collidepoint((x,y)) :
        bouton_exit = generate_rect_button("assets/bouton/bouton_exit.png", (45, 445), (180, 55))
    else:
        bouton_exit = generate_rect_button("assets/bouton/bouton_exit.png", (50, 450), (170, 45))

    if bouton_retour[1].collidepoint((x,y)) :
        bouton_retour = generate_rect_button("assets/bouton/bouton_retour.png", (25, 645), (180, 55))
    else:
        bouton_retour = generate_rect_button("assets/bouton/bouton_retour.png", (30, 650), (170, 45))

    #Stats :
    if game.stat == "menu":
        menu()
        '''Gravite'''
        fenetre.blit(game.player.image,game.player.rect)
        game.player.animated(1)
        fenetre.blit(socle[0], socle[1])
        index_gravite += 1
        if tab_gravite[index_gravite] == "True" :
            index_gravite = 0
            gravite(game.player.rect, 150, (830, 100),1) #256, 412
            gravite(socle[1], 100, (700, 570), 1)
        '''Gravite'''
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
            if game.stat == "game" :
                if bouton_retour[1].collidepoint(event.pos) :
                    bruitage_reculer.play()
                    game.stat = "menu"
            if game.stat == "menu" :
                if bouton_play[1].collidepoint(event.pos):
                    bruitage_avancer.play()
                    game.stat="game"
                    print("lancement du jeu!")
                elif bouton_settings[1].collidepoint(event.pos):
                    bruitage_avancer.play()
                    game.stat="options"
                elif bouton_exit[1].collidepoint(event.pos):
                    bruitage_avancer.play()
                    pygame.quit()
                    boucle = False
                    print("Closing Project ...")
            elif game.stat == "options" :
                if bouton_retour[1].collidepoint(event.pos) :
                    bruitage_reculer.play()
                    game.stat = "menu"
