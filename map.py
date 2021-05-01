import pygame

class Blocks():
    def __init__(self):
        loadimage = lambda filename: pygame.transform.scale(pygame.image.load("assets/texture/"+filename+".png"), (48, 48))
        self.blocksid = {"vide": 0, "roche_big": 1, "roche_small" : 2, "buisson_big" :3, "buisson_small": 4, "herbe_gauche" : 5, "herbe_droite" : 6, "terre_gauche" : 7, "terre_haut" : 8, "terre_droite" : 9, "terre_pleine" : 10, "terre_diagonale_gauche": 11, "terre_diagonale_droite" : 12}
        self.blockstextures= {0: loadimage("vide"), 1: loadimage("Decor/Rock/rock_1"), 2: loadimage("Decor/Rock/rock_2"), 3: loadimage("Decor/Bush/bush_1"), 4: loadimage("Decor/Bush/bush_2"), 5 : loadimage("Tile/Grass/grass_1"), 6 : loadimage("Tile/Grass/grass_2"), 7 : loadimage("Tile/Ground/ground_1"), 8 : loadimage("Tile/Ground/ground_2"), 9 : loadimage("Tile/Ground/ground_3"), 10 : loadimage("Tile/Ground/ground_11"), 11: loadimage("Tile/Ground/ground_5"), 12 : loadimage("Tile/Ground/ground_7"), 13 : loadimage("Tile/Ground/ground_4"), 14 : loadimage("Tile/Ground/ground_6"), 15 : loadimage("Tile/Ground/ground_8"), 16 : loadimage("Tile/Ground/ground_9"), 17 : loadimage("Tile/Ground/ground_10"), 18 : loadimage("Tile/Grass/grass_3"), 19 : loadimage("Tile/Grass/grass_4"), 20 : loadimage("Tile/Grass/grass_5")}

class Spawn :
    def __init__(self, x, y) :
        self.spawn = [x, y]

    def change_pos(self) :
        self.spawn[0] = (pygame.mouse.get_pos()[0] - posx_edit_map) //48
        self.spawn[1] = (pygame.mouse.get_pos()[1] - posy_edit_map) //48

blocks = Blocks()

class Map():
    def __init__(self, width, height, mapname) :
        self.width = width
        self.height = height
        self.blockmaplayer0 = [[0 for i in range (self.height)] for i in range (self.width)]
        self.blockmaplayer1 = [[0 for i in range (self.height)] for i in range (self.width)]
        self.blockmaplayer2 = [[0 for i in range (self.height)] for i in range (self.width)]
        self.spawn = Spawn(0, self.height//2)
        self.map_import(mapname)

    def setblock(self, layer,x, y, blockid):
        try:
            layer[x][y] = blockid
        except IndexError:
            print("Hors Map")

    def map_export(self, filename):
        mapexport = open("maps/"+filename+"/maplayer0.txt", "w")
        mapexport.write(str(self.blockmaplayer0))
        mapexport.close()
        mapexport = open("maps/"+filename+"/maplayer1.txt", "w")
        mapexport.write(str(self.blockmaplayer1))
        mapexport.close()
        mapexport = open("maps/"+filename+"/maplayer2.txt", "w")
        mapexport.write(str(self.blockmaplayer2))
        mapexport.close()

    def map_import(self, filename):
        mapimport = open("maps/"+filename+"/maplayer0.txt", "r")
        self.blockmaplayer0 = list(eval(mapimport.read()))
        mapimport.close()
        mapimport = open("maps/"+filename+"/maplayer1.txt", "r")
        self.blockmaplayer1 = list(eval(mapimport.read()))
        mapimport.close()
        mapimport = open("maps/"+filename+"/maplayer2.txt", "r")
        self.blockmaplayer2 = list(eval(mapimport.read()))
        mapimport.close()

    def map_create(self, filename):
        blockmaplayer0 = [[0 for i in range (self.height)] for i in range (self.width)]
        blockmaplayer1 = [[0 for i in range (self.height)] for i in range (self.width)]
        blockmaplayer2 = [[0 for i in range (self.height)] for i in range (self.width)]
        mapexport = open("maps/"+filename+"/maplayer0.txt", "w")
        mapexport.write(str(blockmaplayer0))
        mapexport.close()
        mapexport = open("maps/"+filename+"/maplayer1.txt", "w")
        mapexport.write(str(blockmaplayer1))
        mapexport.close()
        mapexport = open("maps/"+filename+"/maplayer2.txt", "w")
        mapexport.write(str(blockmaplayer2))
        mapexport.close()
