import pygame
from player import Player
from coffre import Coffre
from monstre import Monstre
from map import *
from setting import Settings


class Game :
    def __init__(self):
        self.keys = {}
        self.all_coffre = pygame.sprite.Group()
        self.all_monstre = pygame.sprite.Group()
        self.player = Player(self)
        self.all_coffre.add(Coffre(self))
        self.all_monstre.add(Monstre(self))
        self.lon,self.lar = 64,64
        self.map = Map(self.lon, self.lar, "map1")
        self.stat = "menu"
        self.index = 0
        self.all_rect = []
        for x in range(len(self.map.blockmaplayer0)):
            for y in range(len(self.map.blockmaplayer0[x])):
                if self.map.blockmaplayer0[x][y] != 0:
                    self.all_rect.append(pygame.Rect(x * 48, y * 48, 48, 48))
        self.air_timer = 0
        self.setting = Settings()

        #Pos map :
        self.cam = [0,0]


    def check_collision(self, sprite, group): #FOnction qui retrun True si il y a collision entre sprite et group
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask) #sprite / group / Oui ou non détruire entité si il y a collision

    def check_collision_sprite(self, rect1, rect2): #FOnction qui retrun True si il y a collision entre sprite et group
        return pygame.sprite.collide_rect(rect1, rect2) #sprite / group / Oui ou non détruire entité si il y a collision

    def collision_test(self, rect, tiles):
        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)
        return hit_list

    def move(self, rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = self.collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        if not self.player.is_jump:
            rect.y += movement[1]
        hit_list = self.collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types
