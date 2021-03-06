#!/usr/bin/env python3

""" Cahier des charges:

    Principe du jeu:

    modules :
    - random (pour les random et autres)
    - pygame_gui eventuellement pour des popups (ajouter des pages)

Elements a dev:
    -physiques
    -gestion des monstres (IA)
    -gestion coffres armes et menu
    -gestion du personnage(vie, inventaire, etc)


"""


#Importations :
import pygame
import time
from random import *
from pygame.locals import *
import os

from game import Game
from map import *
import shutil

#Création de la fenêtre :
fenetre_width, fenetre_height = 1290, 723  #1290 / 723
pygame.display.set_caption("Titre jeu")
fenetre = pygame.display.set_mode((fenetre_width, fenetre_height))

#Initialisation :
pygame.init()

#Création game :
game = Game()

#TXT
font = pygame.font.SysFont("aquakanattc", 20, True, False)
text_edit_font = pygame.font.SysFont("aquakanattc", 25, True, False)

#Fonctions :

def generate_rect(lien, pos) :
    new_image = pygame.image.load(lien).convert()
    new_image.set_colorkey((0, 0, 0))
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
    new_image = pygame.image.load(lien).convert()
    new_image.set_colorkey((0, 0, 0))
    new_image = pygame.transform.scale(new_image, (dim[0], dim[1]))
    new_image_rect = new_image.get_rect()
    new_image_rect.x = pos[0]
    new_image_rect.y = pos[1]
    return [new_image, new_image_rect]

#Music :
musique_menu = pygame.mixer.Sound("assets/music/musique_accueil.ogg")
musique_menu.set_volume(game.setting.volume)
musique_menu.play(-1)

#Bruitages :
bruitage_avancer = pygame.mixer.Sound("assets/music/bruitage_avancer.ogg")
bruitage_reculer = pygame.mixer.Sound("assets/music/bruitage_retour.ogg")
bruitage_avancer.set_volume(5)
bruitage_reculer.set_volume(5)

img_spawn = pygame.image.load("assets/texture/spawn.png")

#Menu :
background = pygame.image.load("assets/fond_ecran.png")
background = pygame.transform.scale(background, (fenetre_width, fenetre_height))
images_boutons = pygame.image.load("assets/bouton/boutons.png")

#Edition :
image_spawn = pygame.image.load("assets/texture/spawn.png")
image_coffre = pygame.image.load("assets/coffre/coffre.png")
image_monstre1 = pygame.image.load("assets/monstre/monstre.png")
image_monstre2 = pygame.image.load("assets/monstre/monstre.png")
image_monstre3 = pygame.image.load("assets/monstre/monstre.png")
list_image_edit = [image_spawn, image_coffre, image_monstre1, image_monstre2, image_monstre3]
for i in range(len(list_image_edit)) :
    list_image_edit[i] = pygame.transform.scale(list_image_edit[i], (40, 40))
color_text = (255, 255, 255)
text_spawn = text_edit_font.render('s', True, color_text)
text_coffre = text_edit_font.render('c', True, color_text)
text_monstre1 = text_edit_font.render('i', True, color_text)
text_monstre2 = text_edit_font.render('o', True, color_text)
text_monstre3 = text_edit_font.render('p', True, color_text)
list_text_edit = [text_spawn, text_coffre, text_monstre1, text_monstre2, text_monstre3]


#Boutons :
bouton_play = generate_rect_button("assets/bouton/bouton_play.png", (250, 150), (170, 45))
bouton_settings = generate_rect_button("assets/bouton/bouton_option.png", (250, 350), (170, 45))
bouton_exit = generate_rect_button("assets/bouton/bouton_exit.png", (250, 550), (170, 45))
bouton_retour = generate_rect_button("assets/bouton/bouton_retour.png", (30, 650), (170, 45))
bouton_continue = generate_rect_button("assets/bouton/continue.png", (550, 300), (170, 45))
bouton_edit = generate_rect_button("assets/bouton/edit.png", (150, 300), (170, 45))
bouton_create_map = generate_rect_button("assets/bouton/create_map.png",(fenetre.get_size()[0]-240, 650), (170, 45))

#Gravité :
socle = generate_rect("assets/support.png", (750, 570))
socle[0] = pygame.transform.scale(socle[0], (400, 100))
delay = 5
tab_gravite = ["False"] * delay
tab_gravite.append("True")

index_gravite = 0

#édition
posx_edit_map = 0
posy_edit_map = 0
actual_block = 1
cadre = pygame.image.load("assets/cadre.png")

#map selection
map_selectionee = 0

def makemaptxt(font):
    texte_maps = pygame.Surface((300, fenetre.get_size()[1]))
    texte_maps.fill((25,75,50))
    for i in range(len(os.listdir("./maps/"))):
        text_surface = font.render(str(os.listdir("./maps/")[i]), True, ( 52, 188, 44 ))
        if i != map_selectionee:
            texte_maps.blit(text_surface, [30, 30+i*30])
        else:
            texte_map_select = pygame.Surface((300, 14))
            texte_map_select.fill(( 24, 72, 21 ))
            texte_map_select.blit(text_surface, [0, 0])
            texte_maps.blit(texte_map_select, [30, 30+i*30])
    return(texte_maps)

texte_maps = makemaptxt(font)


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
    fenetre.blit(texte_maps, [fenetre.get_size()[0]-300, 0])
    fenetre.blit(bouton_create_map[0], bouton_create_map[1])
    if game.is_input :
        fenetre.blit(text_Text, (1050, 600))
        fenetre.blit(phrase_unicode, (1090, 600))

def playing() :
    game.player.animated()
    game.cam[0] += (game.player.rect.x-game.cam[0]-(fenetre_width//2))/10
    game.cam[1] += (game.player.rect.y-game.cam[1]-(fenetre_height//2))/10
    fenetre.blit(background, (0, 0))
    for x in range(len(game.map.blockmaplayer0)):
        for y in range(len(game.map.blockmaplayer0[x])):
            if game.map.blockmaplayer0[x][y] != 0:
                fenetre.blit(game.map.blocks.blockstextures[game.map.blockmaplayer0[x][y]], (x*48-game.cam[0], y*48-game.cam[1]))
    for x in range(len(game.map.blockmaplayer1)):
        for y in range(len(game.map.blockmaplayer1[x])):
            if game.map.blockmaplayer1[x][y] != 0:
                fenetre.blit(game.map.blocks.blockstextures[game.map.blockmaplayer1[x][y]], (x*48-game.cam[0], y*48-game.cam[1]))
    for x in range(len(game.map.blockmaplayer2)):
        for y in range(len(game.map.blockmaplayer2[x])):
            if game.map.blockmaplayer2[x][y] != 0:
                #fenetre.blit(game.map.blocks.blockstextures[game.map.blockmaplayer2[x][y]], (x*48-game.cam[0], y*48-game.cam[1]))
                if game.map.blockmaplayer2[x][y] == 99:
                    fenetre.blit(game.coffre.image, (x*48+posx_edit_map, y*48+posy_edit_map))
    fenetre.blit(img_spawn, (game.map.spawn.spawn[0]*48-game.cam[0], game.map.spawn.spawn[1]*48-game.cam[1]))

    #Coffres :
    for coffre in game.all_coffre:
        if coffre.is_loot:
            coffre.lout(fenetre, background)

    #Monstres :
    '''
    for monstre in game.all_monstre :
        monstre.show(fenetre, )
        monstre.move()
    '''

    fenetre.blit(bouton_retour[0], bouton_retour[1])
    fenetre.blit(game.player.image, (game.player.rect.x-game.cam[0], game.player.rect.y-game.cam[1]))
    game.player.movement = [0,0]
    game.player.mode = "player"
    if game.keys.get(game.setting.touche["haut"]) :
        game.player.mode = "player_jump"
        game.player.saut()
    if game.keys.get(game.setting.touche["droite"]) :
        game.player.droite()
        game.player.mouvement = "droite"
    elif game.keys.get(game.setting.touche["gauche"]) :
        game.player.gauche()
        game.player.mouvement = "gauche"
    else :
        game.player.mouvement = ""



    game.player.movement[1] += game.player.y_gravite
    game.player.y_gravite += 0.6
    if game.player.y_gravite > 15:
        game.player.y_gravite = 15


    game.player.rect, collisions = game.move(game.player.rect, game.player.movement, game.all_rect)

    if collisions['bottom']:
        game.player.y_gravite = 0
        game.air_timer = 0
    elif collisions['top']:
        game.player.y_gravite = 15
    else:
        game.air_timer += 1


def editing_map() :
    global posx_edit_map
    global posy_edit_map
    global actual_block
    fenetre.blit(background, (0, 0))
    fenetre.blit(cadre, (fenetre.get_size()[0]-250, 38))
    for x in range(len(game.map.blockmaplayer0)):
        for y in range(len(game.map.blockmaplayer0[x])):
            if game.map.blockmaplayer0[x][y] != 0:
                fenetre.blit(game.map.blocks.blockstextures[game.map.blockmaplayer0[x][y]], (x*48+posx_edit_map, y*48+posy_edit_map))
    for x in range(len(game.map.blockmaplayer1)):
        for y in range(len(game.map.blockmaplayer1[x])):
            if game.map.blockmaplayer1[x][y] != 0:
                fenetre.blit(game.map.blocks.blockstextures[game.map.blockmaplayer1[x][y]], (x*48+posx_edit_map, y*48+posy_edit_map))
    for x in range(len(game.map.blockmaplayer2)):
        for y in range(len(game.map.blockmaplayer2[x])):
            if game.map.blockmaplayer2[x][y] != 0:
                #fenetre.blit(game.map.blocks.blockstextures[game.map.blockmaplayer2[x][y]], (x*48+posx_edit_map, y*48+posy_edit_map))
                if game.map.blockmaplayer2[x][y] == 99:
                    fenetre.blit(game.coffre.image, (x*48+posx_edit_map, y*48+posy_edit_map))
    fenetre.blit(img_spawn, (game.map.spawn.spawn[0]*48+posx_edit_map, game.map.spawn.spawn[1]*48+posy_edit_map))

    fenetre.blit(bouton_retour[0], bouton_retour[1])

    #Items à ajouter edit :
    y = 120
    for loop in range(len(list_image_edit)) :
        fenetre.blit(list_image_edit[loop], (1240, y))
        fenetre.blit(list_text_edit[loop], (1210, y+10))
        y += 60


    speed = 20
    if game.keys.get(pygame.K_LEFT):
        if posx_edit_map < 0:
            posx_edit_map += speed

    if game.keys.get(pygame.K_RIGHT):
        x = game.lon*48-fenetre_width-48
        x = -x

        if posx_edit_map > x:
            posx_edit_map -= speed

    if game.keys.get(pygame.K_UP):
        if posy_edit_map < 0:
            posy_edit_map += speed

    if game.keys.get(pygame.K_DOWN):
        y = game.lar*48-fenetre_height
        y= -y
        if posy_edit_map>y:
            posy_edit_map -= speed

    blockundermousex = (pygame.mouse.get_pos()[0] - posx_edit_map) //48
    blockundermousey = (pygame.mouse.get_pos()[1] - posy_edit_map) //48
    if pygame.mouse.get_pressed()[2]:
        if actual_block in game.map.listlayer2:
            game.map.setblock(game.map.blockmaplayer2, blockundermousex, blockundermousey, actual_block)
        elif actual_block in game.map.listlayer1:
            game.map.setblock(game.map.blockmaplayer1, blockundermousex, blockundermousey, actual_block)
        elif actual_block in game.map.listlayer0:
            game.map.setblock(game.map.blockmaplayer0, blockundermousex, blockundermousey, actual_block)
    elif pygame.mouse.get_pressed()[0]:
        if game.map.blockmaplayer2[blockundermousex][blockundermousey]:
            game.map.setblock(game.map.blockmaplayer2, blockundermousex, blockundermousey, 0)
        elif game.map.blockmaplayer1[blockundermousex][blockundermousey]:
            game.map.setblock(game.map.blockmaplayer1, blockundermousex, blockundermousey, 0)
        else:
            game.map.setblock(game.map.blockmaplayer0, blockundermousex, blockundermousey, 0)

    ''' Edition blocks specials '''
    if game.keys.get(pygame.K_s):
        game.map.spawn.change_pos(blockundermousex, blockundermousey)
    elif game.keys.get(pygame.K_c) :
        game.map.blockmaplayer2[blockundermousex][blockundermousey] = 99
    elif game.keys.get(pygame.K_i) :
        pass
    elif game.keys.get(pygame.K_o) :
        pass
    elif game.keys.get(pygame.K_p) :
        pass



    try:
        fenetre.blit(pygame.transform.scale(game.map.blocks.blockstextures[actual_block], (32, 32)), [fenetre.get_size()[0]-143, 49])
    except:
        pass


    if actual_block != 1:
        fenetre.blit(pygame.transform.scale(game.map.blocks.blockstextures[actual_block-1], (32, 32)), [fenetre.get_size()[0]-200, 50])
        fenetre.blit(pygame.transform.scale(game.map.blocks.blockstextures[actual_block-2], (32, 32)), [fenetre.get_size()[0]-250, 50])
    else:
        fenetre.blit(pygame.transform.scale(game.map.blocks.blockstextures[len(game.map.blocks.blockstextures)-1], (32, 32)), [fenetre.get_size()[0]-200, 50])
        fenetre.blit(pygame.transform.scale(game.map.blocks.blockstextures[len(game.map.blocks.blockstextures)-2], (32, 32)), [fenetre.get_size()[0]-250, 50])
    try:
        fenetre.blit(pygame.transform.scale(game.map.blocks.blockstextures[actual_block+1], (32, 32)), [fenetre.get_size()[0]-100, 50])
    except:
        fenetre.blit(pygame.transform.scale(game.map.blocks.blockstextures[1], (32, 32)), [fenetre.get_size()[0]-100, 50])
    try:
        fenetre.blit(pygame.transform.scale(game.map.blocks.blockstextures[actual_block+2], (32, 32)), [fenetre.get_size()[0]-50, 50])
    except:
        fenetre.blit(pygame.transform.scale(game.map.blocks.blockstextures[2], (32, 32)), [fenetre.get_size()[0]-50, 50])

#Map :
text_map = ""
phrase_unicode = font.render(text_map, True, (0, 0, 0))
text_Text = font.render('Map : ', True, (0, 0, 0))

#FPS :
clock = pygame.time.Clock()

#Boucle principale :
boucle = True
while boucle:
    #Mouse :
    x, y = pygame.mouse.get_pos()
    text_FPS = font.render(str(int(clock.get_fps())), True, (0, 0, 0))  # non parce que c'est mal dev :kappa:


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

    if bouton_create_map[1].collidepoint((x,y)) :
        bouton_create_map = generate_rect_button("assets/bouton/create_map.png",(fenetre.get_size()[0]-245, 645), (180, 55))
    else:
        bouton_create_map = generate_rect_button("assets/bouton/create_map.png",(fenetre.get_size()[0]-240, 650), (170, 45))

    if bouton_edit[1].collidepoint((x,y)) :
        bouton_edit = generate_rect_button("assets/bouton/edit.png", (145, 295), (180, 55))
    else:
        bouton_edit = generate_rect_button("assets/bouton/edit.png", (150, 300), (170, 45))

    if bouton_continue[1].collidepoint((x,y)) :
        bouton_continue = generate_rect_button("assets/bouton/continue.png", (545, 295), (180, 55))
    else:
        bouton_continue = generate_rect_button("assets/bouton/continue.png", (550, 300), (170, 45))

    #Stats :
    if game.stat == "menu":
        menu()
        '''Gravite'''
        fenetre.blit(game.player.image,[875, 265])
        game.player.mode = "player_run"
        game.player.animated()
        fenetre.blit(socle[0], socle[1])
        index_gravite += 1
        if tab_gravite[index_gravite] == "True" :
            index_gravite = 0
            gravite(game.player.rect, 150, (830, 100),1)
            gravite(socle[1], 100, (700, 570), 1)
        '''Gravite'''
    if game.stat == "options" :
        options()
        #Slider :
        if pygame.mouse.get_pressed()[0] and game.setting.curseur_FPS.collidepoint(event.pos) and x >= 225 and x <= 1020 or pygame.mouse.get_pressed()[0] and game.setting.slider_FPS.collidepoint(event.pos) and x >= 225 and x <= 1020:
            game.setting.curseur_FPS.x = x - 20
            game.setting.change_FPS()

            game.setting.text_fps = game.setting.font.render(str(game.setting.fps), True, game.setting.color_text)


        if pygame.mouse.get_pressed()[0] and game.setting.curseur_VOLUME.collidepoint(event.pos) and x >= 225 and x <= 1020 or pygame.mouse.get_pressed()[0] and game.setting.slider_VOLUME.collidepoint(event.pos) and x >= 225 and x <= 1020:
            game.setting.curseur_VOLUME.x = x - 20
            game.setting.change_volume()
            musique_menu.set_volume(game.setting.volume)

            game.setting.text_volume = game.setting.font.render(str(int(game.setting.volume * 10)), True, game.setting.color_text)
    if game.stat == "game" :
        game.player.mode = "player_run"
        jeux()

    if game.stat == "editing_map" :
        editing_map()
    if game.stat == "playing" :
        playing()
    fenetre.blit(text_FPS, (10, 10))
    pygame.display.flip()

    for event in pygame.event.get() :

        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            boucle = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if game.stat == "game" :
                game.keys[event.key] = True
                if game.is_input:
                    if event.key != pygame.K_BACKSPACE :

                        if len(text_map) < 15:
                            text_map += event.unicode
                    else:
                        text_map = text_map[:-1]

                    phrase_unicode = font.render(text_map, True, (0, 0, 0))

                    if event.key == pygame.K_RETURN:
                        game.is_input = False
                        game.map.map_create(text_map)
                        texte_maps = makemaptxt(font)
                        text_map = ""
                        phrase_unicode = font.render(text_map, True, (0, 0, 0))

                    '''SUPPR MAPS: '''
                if event.key == pygame.K_BACKSPACE:
                    shutil.rmtree(("./maps/"+os.listdir("./maps/")[map_selectionee]))
                    map_selectionee = 0
                    texte_maps = makemaptxt(font)


            if game.stat == 'editing_map':
                if event.key == pygame.K_q:
                    if actual_block > 1:
                        actual_block -=1
                    else:
                        actual_block = len(game.map.blocks.blockstextures)-1
                if event.key == pygame.K_d :
                    if actual_block < len(game.map.blocks.blockstextures)-1:
                        actual_block += 1
                    else:
                        actual_block = 1

        if event.type == pygame.KEYUP:
            game.keys[event.key] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.stat == "game" :
                if bouton_create_map[1].collidepoint(event.pos):
                    game.is_input = True
                if not game.is_input:
                    if bouton_retour[1].collidepoint(event.pos):
                        bruitage_reculer.play()
                        game.player.resize((156, 212))
                        game.stat = "menu"
                    if bouton_continue[1].collidepoint(event.pos):
                        game.map.map_import( os.listdir("./maps/")[map_selectionee])
                        game.all_rect = []
                        for x in range(len(game.map.blockmaplayer0)):
                            for y in range(len(game.map.blockmaplayer0[x])):
                                if game.map.blockmaplayer0[x][y] != 0:
                                    game.all_rect.append(pygame.Rect(x * 48, y * 48, 48, 48))
                        game.player.resize((56, 111)) #111
                        game.player.rect = pygame.Rect(0, 0, 56, 111)
                        bruitage_avancer.play()
                        game.stat = "playing"
                        game.player.rect.x = list(eval(open("maps/"+os.listdir("./maps/")[map_selectionee]+"/spawn.txt").read()))[0]*48 - 24
                        game.player.rect.y = list(eval(open("maps/"+os.listdir("./maps/")[map_selectionee]+"/spawn.txt").read()))[1]*48 - 96
                    if bouton_edit[1].collidepoint(event.pos):
                        game.map.map_import( os.listdir("./maps/")[map_selectionee])
                        bruitage_avancer.play()
                        game.stat = "editing_map"

                if x >= fenetre.get_size()[0]-300:
                    try:
                        if os.listdir("./maps/")[(y-30)//30]:
                            map_selectionee = (y-30)//30
                    except:
                        pass
                    texte_maps = makemaptxt(font)


            if game.stat == "menu" :
                game.player.resize((136, 212))
                if bouton_play[1].collidepoint(event.pos):
                    bruitage_avancer.play()
                    game.stat="game"
                elif bouton_settings[1].collidepoint(event.pos):
                    bruitage_avancer.play()
                    game.stat="options"
                    game.setting.pos_FPS()
                    game.setting.pos_volume()
                elif bouton_exit[1].collidepoint(event.pos):
                    bruitage_avancer.play()
                    boucle = False
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
                    if game.stat== "editing_map":
                        for x in range(len(game.map.blockmaplayer0)):
                            for y in range(len(game.map.blockmaplayer0[x])):
                                if game.map.blockmaplayer0[x][y] != 0:
                                    game.all_rect.append(pygame.Rect(x * 48, y * 48, 48, 48))
                        game.map.map_export(os.listdir("./maps/")[map_selectionee])
                    game.stat = "game"

    clock.tick(game.setting.fps)

game.setting.extract_fps()
game.setting.extract_volume()
game.map.map_export(os.listdir("./maps/")[map_selectionee])
pygame.quit()
