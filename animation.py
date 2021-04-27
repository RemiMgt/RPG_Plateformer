import pygame

class Animation(pygame.sprite.Sprite):

    def __init__(self, taille_tab, n_image, temps):
        super().__init__()
        if taille_tab != n_image:
            print("erreur le nombre dimage et de taille ne sont pas les meme")
        self.n_image = n_image
        self.t_b = taille_tab
        self.tab = self.load()
        self.index = [0] * len(taille_tab)
        self.image = pygame.image.load('assets/player/'+n_image[0]+".png")
        self.image = pygame.transform.scale(self.image, (356, 512))
        self.tab_delay = []
        for i in range(len(temps)):
            self.tab_delay.append(["False"]*temps[i])
            self.tab_delay[i].append("True")
        self.index_delay = [0]*len(temps)

    def animated(self, i):
        self.index_delay[i] += 1
        if self.tab_delay[i][self.index_delay[i]] == "True" :
            self.index_delay[i] = 0
            if self.index[i] == len(self.tab[i]) - 1 :
                self.index[i] = 0
            else:
                self.index[i] += 1
                self.image = self.tab[i][self.index[i]]
                self.image = pygame.transform.scale(self.image, (356, 512))

    def load(self):
        images =[]
        for i in range(len(self.t_b)):
            images.append([])
            path =f'assets/{self.n_image[i]}/{self.n_image[i]}/{self.n_image[i]}'
            for y in range(1,self.t_b[i]+1):
                images[i].append(pygame.transform.scale(pygame.image.load(path+str(y)+".gif"), (300,400)))
        return images
