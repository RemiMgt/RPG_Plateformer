#!/usr/bin/env python3

#Importations :
import pygame
import random
from game import Game 

#Initialisation :
pygame.init()

#Création fenêtre :
fenetre_width = 1500
fenetre_height = 1000
pygame.display.set_caption("Ttire jeux") 
fenetre = pygame.display.set_mode((fenetre_width, fenetre_height))

#Création game :
game = Game()

#Boucle principale :
boucle = True
while boucle :

    pygame.display.flip()

    for event in pygame.event.get() :

        if event.type == pygame.QUIT :
            pygame.quit()
            boucle = False
            print("Closing Project ...")

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_ESCAPE :
                pygame.quit()
                boucle = False
                print("Closing Project ...")