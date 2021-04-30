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
import sys

from game import Game
from map import *

#Initialisation :
pygame.init()

#Création game :
game = Game()

#Music :
musique_menu = pygame.mixer.Sound("assets/music/musique_accueil.ogg")
musique_menu.set_volume(game.setting.volume) #0.1
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
bouton_continue = generate_rect_button("assets/bouton/continue.jpg", (800, 300), (200, 60))
bouton_edit = generate_rect_button("assets/bouton/edit.jpg", (300, 300), (200, 60))

#Gravité :
socle = generate_rect("assets/support.png", (750, 570))
socle[0] = pygame.transform.scale(socle[0], (400, 100))
delay = 5
tab_gravite = ["False"] * delay
tab_gravite.append("True")

index_gravite = 0

#Map :
lon,lar = 64,64
map = Map(lon, lar, "map1")

#édition
posx_edit_map = 0
posy_edit_map = 0
actual_block = 1

#TXT
font = pygame.font.SysFont("aquakanattc", 20, True, False)
text_surface = font.render("", True, (255, 0, 0))
surface = pygame.Surface((text_surface.get_width()+20, text_surface.get_height()+20))
surface.fill((0,0,255))
surface.blit(text_surface, [surface.get_width()/2 - text_surface.get_width()/2,
                            surface.get_height()/2 - text_surface.get_height()/2])


#Fonctions jeux:
def menu() :
    fenetre.blit(background, (0, 0))
    fenetre.blit(bouton_exit[0], bouton_exit[1])
    fenetre.blit(bouton_play[0], bouton_play[1])
    fenetre.blit(bouton_settings[0], bouton_settings[1])

def options():
    fenetre.blit(background, (0, 0))
    fenetre.blit(bouton_retour[0], bouton_retour[1])
    game.setting.draw(fenetre)

def jeux():
    fenetre.blit(background, (0, 0))
    fenetre.blit(bouton_continue[0], bouton_continue[1])
    fenetre.blit(bouton_edit[0], bouton_edit[1])
    fenetre.blit(bouton_retour[0], bouton_retour[1])

def playing() :
    posx = 0
    posy = 0
    fenetre.blit(background, (0, 0))
    for x in range(len(map.blockmaplayer0)):
        for y in range(len(map.blockmaplayer0[x])):
            fenetre.blit(blocks.blockstextures[map.blockmaplayer0[x][y]], (x*48+posx, y*48+posy))
    for x in range(len(map.blockmaplayer1)):
        for y in range(len(map.blockmaplayer1[x])):
            fenetre.blit(blocks.blockstextures[map.blockmaplayer1[x][y]], (x*48+posx, y*48+posy))
    for x in range(len(map.blockmaplayer2)):
        for y in range(len(map.blockmaplayer2[x])):
            fenetre.blit(blocks.blockstextures[map.blockmaplayer2[x][y]], (x*48+posx, y*48+posy))
    fenetre.blit(bouton_retour[0], bouton_retour[1])


def editing_map() :
    global posx_edit_map
    global posy_edit_map
    global actual_block
    fenetre.blit(background, (0, 0))
    for x in range(len(map.blockmaplayer0)):
        for y in range(len(map.blockmaplayer0[x])):
            fenetre.blit(blocks.blockstextures[map.blockmaplayer0[x][y]], (x*48+posx_edit_map, y*48+posy_edit_map))
    for x in range(len(map.blockmaplayer1)):
        for y in range(len(map.blockmaplayer1[x])):
            fenetre.blit(blocks.blockstextures[map.blockmaplayer1[x][y]], (x*48+posx_edit_map, y*48+posy_edit_map))
    for x in range(len(map.blockmaplayer2)):
        for y in range(len(map.blockmaplayer2[x])):
            fenetre.blit(blocks.blockstextures[map.blockmaplayer2[x][y]], (x*48+posx_edit_map, y*48+posy_edit_map))
    fenetre.blit(bouton_retour[0], bouton_retour[1])

    speed = 20
    try:
        if game.keys[pygame.K_LEFT]:
            if posx_edit_map < 0:
                posx_edit_map += speed
    except KeyError:
        pass
    try:
        if game.keys[pygame.K_RIGHT]:
            x = lon*48-fenetre_width-48
            x = -x

            if posx_edit_map > x:
                posx_edit_map -= speed
    except KeyError:
        pass
    try:
        if game.keys[pygame.K_UP]:


            if posy_edit_map < 0:
                posy_edit_map += speed
    except KeyError:
        pass
    try:
        if game.keys[pygame.K_DOWN]:
            y = lar*48-fenetre_height
            y= -y
            if posy_edit_map>y:
                posy_edit_map -= speed
    except KeyError:
        pass

    blockundermousex = (pygame.mouse.get_pos()[0] - posx_edit_map) //48
    blockundermousey = (pygame.mouse.get_pos()[1] - posy_edit_map) //48
    if pygame.mouse.get_pressed()[2]:
        if map.blockmaplayer1[blockundermousex][blockundermousey]:
            map.setblock(map.blockmaplayer2, blockundermousex, blockundermousey, actual_block)
        elif map.blockmaplayer0[blockundermousex][blockundermousey]:
            map.setblock(map.blockmaplayer1, blockundermousex, blockundermousey, actual_block)
        else:
            map.setblock(map.blockmaplayer0, blockundermousex, blockundermousey, actual_block)
    elif pygame.mouse.get_pressed()[0]:
        if map.blockmaplayer2[blockundermousex][blockundermousey]:
            map.setblock(map.blockmaplayer2, blockundermousex, blockundermousey, 0)
        elif map.blockmaplayer1[blockundermousex][blockundermousey]:
            map.setblock(map.blockmaplayer1, blockundermousex, blockundermousey, 0)
        else:
            map.setblock(map.blockmaplayer0, blockundermousex, blockundermousey, 0)

    try:
        fenetre.blit(pygame.transform.scale(blocks.blockstextures[actual_block], (32, 32)), [fenetre.get_size()[0]-143, 49])
    except:
        pass

    if actual_block != 1:
        fenetre.blit(pygame.transform.scale(blocks.blockstextures[actual_block-1], (32, 32)), [fenetre.get_size()[0]-184, 49])
        fenetre.blit(pygame.transform.scale(blocks.blockstextures[actual_block-2], (32, 32)), [fenetre.get_size()[0]-234, 49])
    else:
        fenetre.blit(pygame.transform.scale(blocks.blockstextures[len(blocks.blockstextures)-1], (32, 32)), [fenetre.get_size()[0]-184, 49])
        fenetre.blit(pygame.transform.scale(blocks.blockstextures[len(blocks.blockstextures)-2], (32, 32)), [fenetre.get_size()[0]-234, 49])
    try:
        fenetre.blit(pygame.transform.scale(blocks.blockstextures[actual_block+1], (32, 32)), [fenetre.get_size()[0]-103, 49])
    except:
        fenetre.blit(pygame.transform.scale(blocks.blockstextures[1], (32, 32)), [fenetre.get_size()[0]-103, 49])
    try:
        fenetre.blit(pygame.transform.scale(blocks.blockstextures[actual_block+2], (32, 32)), [fenetre.get_size()[0]-53, 49])
    except:
        fenetre.blit(pygame.transform.scale(blocks.blockstextures[2], (32, 32)), [fenetre.get_size()[0]-53, 49])

#FPS :
FPS = game.setting.fps
frame_delay = 1000//FPS

#FPS :
FPS = 30
frame_delay = 1000//FPS

#Boucle principale :
boucle = True
while boucle:
    timeStart = pygame.time.get_ticks()

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
        game.player.mode = "player_run"
        game.player.animated()
        fenetre.blit(socle[0], socle[1])
        index_gravite += 1
        if tab_gravite[index_gravite] == "True" :
            index_gravite = 0
            gravite(game.player.rect, 150, (830, 100),1) #256, 412
            gravite(socle[1], 100, (700, 570), 1)
        '''Gravite'''
    if game.stat == "options" :
        options()
        #Slider :
        if pygame.mouse.get_pressed()[0] and game.setting.curseur_FPS.collidepoint(event.pos) and x >= 225 and x <= 1020 :
            game.setting.curseur_FPS.x = x - 20
        if pygame.mouse.get_pressed()[0] and game.setting.curseur_VOLUME.collidepoint(event.pos) and x >= 225 and x <= 1020 :
            game.setting.curseur_VOLUME.x = x - 20
    if game.stat == "game" :
        jeux()
    if game.stat == "editing_map" :
        editing_map()
    if game.stat == "playing" :
        playing()

    pygame.display.flip()

    for event in pygame.event.get() :

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            boucle = False
            print("Closing Project ...")
            sys.exit()

        if event.type == pygame.KEYDOWN :
            game.keys[event.key] = True
            if game.stat == "playing" :
                if event.key == game.setting.touche["haut"]:
                    print("Saute")
                if event.key == game.setting.touche["droite"] :
                    print("Droite")
                if event.key == game.setting.touche["gauche"] :
                    print("Gauche")
            if event.key == pygame.K_q :
                if actual_block > 1:
                    actual_block -=1
                else:
                    actual_block = len(blocks.blocksid)-1
            if event.key == pygame.K_d :
                if actual_block < len(blocks.blocksid)-1:
                    actual_block += 1
                else:
                    actual_block = 1

        if event.type == pygame.KEYUP:
            game.keys[event.key] = False

        if event.type == pygame.MOUSEBUTTONDOWN :
            if game.stat == "game" :
                if bouton_retour[1].collidepoint(event.pos) :
                    bruitage_reculer.play()
                    game.stat = "menu"
                if bouton_continue[1].collidepoint(event.pos) :
                    bruitage_avancer.play()
                    game.stat = "playing"
                if bouton_edit[1].collidepoint(event.pos) :
                    bruitage_avancer.play()
                    game.stat = "editing_map"

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
                #Boutons touches :
                if game.setting.selection_azerty_rect.collidepoint(event.pos) :
                    game.setting.changing("azerty")
                if game.setting.selection_qwerty_rect.collidepoint(event.pos) :
                    game.setting.changing("qwerty")
                if game.setting.selection_fleche_rect.collidepoint(event.pos) :
                    game.setting.changing("fleche")
            elif game.stat == "editing_map" or game.stat == "playing":
                if bouton_retour[1].collidepoint(event.pos) :
                    bruitage_reculer.play()
                    game.stat = "game"

    timeEnd = pygame.time.get_ticks()  # L'heure à la fin de la création de l'image
    timeFrame = timeEnd - timeStart  # Le temps passé dans la création de l'image qui va s'afficher
    if frame_delay - timeFrame:
        pygame.time.delay(frame_delay - timeFrame)

map.map_export("map1")
