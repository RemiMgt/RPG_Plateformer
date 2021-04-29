import pygame

class Blocks():
    def __init__(self):
        loadimage = lambda filename: pygame.transform.scale(pygame.image.load("assets/texture/"+filename+".png"), (48, 48))
        self.blocksid = {"vide": 0, "roche_big": 1, "roche_small" : 2, "buisson_big" :3, "buisson_small": 4, "herbe_gauche" : 5, "herbe_droite" : 6, "terre_gauche" : 7, "terre_haut" : 8, "terre_droite" : 9, "terre_pleine" : 10, "terre_diagonale_gauche": 11, "terre_diagonale_droite" : 12}
        self.blockstextures= {0: loadimage("vide"), 1: loadimage("Decor/Rock/rock_1"), 2: loadimage("Decor/Rock/rock_2"), 3: loadimage("Decor/Bush/bush_1"), 4: loadimage("Decor/Bush/bush_2"), 5 : loadimage("Tile/Grass/grass_1"), 6 : loadimage("Tile/Grass/grass_2"), 7 : loadimage("Tile/Ground/ground_1"), 8 : loadimage("Tile/Ground/ground_2"), 9 : loadimage("Tile/Ground/ground_3"), 10 : loadimage("Tile/Ground/ground_11"), 11: loadimage("Tile/Ground/ground_5"), 12 : loadimage("Tile/Ground/ground_7")}

blocks = Blocks()

class Map():
    def __init__(self, width, height, blockmaplayer0name, blockmaplayer1name) :
        self.width = width
        self.height = height
        self.blockmaplayer0 = []
        self.map_import(self.blockmaplayer0, blockmaplayer0name)
        self.blockmaplayer1 = [[0 for i in range (self.height)] for i in range (self.width)]
        self.map_import(self.blockmaplayer1, blockmaplayer1name)

    def setblock(self, layer, x, y, blockname):
        try:
            layer[x][y] = blocks.blocksid[blockname]
        except IndexError:
            print("Hors Map")

    def map_export(self, filename, layer):
        mapexport = open("maps/"+filename+".txt", "w")
        mapexport.write(str(layer))
        mapexport.close()

    def map_import(self, layer, filename):
        mapimport = open("maps/"+filename+".txt", "r")
        layer = list(eval(mapimport.read()))
        mapimport.close()
        return layer
