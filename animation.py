import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, dir, path, animation_speed, default_mode, is_gauche = False, gauche = None ,size=None, is_stop=False, group=None):
        super().__init__()

        self.imggauche = ""
        self.dir = dir  # main dir
        self.path = path  # dict as {"under_dir": number_files}
        self.mode = default_mode  # idle, jump, run, etc. MUST be the name of an under dir
        self.animation_speed = animation_speed.copy()
        self.image_index = animation_speed.copy()
        self.is_stop = is_stop
        self.group = group
        if is_gauche == True:
            self.is_gauche = gauche
            self.false = False
        else:
            self.is_gauche = []
            self.false = True
        self.images = self.load(size)  # dict as {"mode": [pygame_surface_images]}
        self.image = self.images[self.mode][0]


    def resize(self, size) :
        self.images = self.load(size)

    def animated(self):
        self.image = self.images[self.mode][int(self.image_index[self.mode])]

        if int(self.image_index[self.mode] + self.animation_speed[self.mode]) >= len(self.images[self.mode]):
            if not self.is_stop:
                self.image_index[self.mode] = 0
            else:
                if self.group is not None:
                    self.group.remove(self)

        else:
            self.image_index[self.mode] += self.animation_speed[self.mode]

    def load(self, size=False):
        images = {}
        for j,under_dir in enumerate(self.path):
            temp = []
            temp_gauche = []
            if self.false:
                self.is_gauche =[False]*self.path[under_dir]
            for i in range(self.path[under_dir]):
                img = pygame.image.load(f"assets/{self.dir}/{under_dir}/{under_dir}{i + 1}.png").convert()
                if self.is_gauche[j] != False:
                    self.imggauche = pygame.transform.flip(img, True, False)

                #img.set_colorkey((0, 0, 0))
                if size is not None:
                    img = pygame.transform.scale(img, size)
                    if self.is_gauche[j] == True:
                        self.imggauche = pygame.transform.scale(self.imggauche, size)
                temp.append(img)
                temp_gauche.append(self.imggauche)
            images[under_dir] = temp
            images[under_dir + "_gauche"] = temp_gauche
            self.image_index[under_dir + "_gauche"] = self.image_index[under_dir]
            self.animation_speed[under_dir + "_gauche"] = self.animation_speed[under_dir]


        return images
