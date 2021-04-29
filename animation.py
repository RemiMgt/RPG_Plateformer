import pygame


class Animation(pygame.sprite.Sprite):

    def __init__(self, taille_tab, dossier, n_image, temps, is_resize=False, size=None, is_stop=False, is_remove=False,
                 group=None):
        super().__init__()
        if len(taille_tab) != len(n_image):
            print("erreur le nombre dimage et de taille ne sont pas les meme")
        self.n_image = n_image
        self.dossier = dossier
        self.size = size
        self.is_resize = is_resize
        self.is_stop = is_stop
        self.is_remove = is_remove
        self.group = group
        self.t_b = taille_tab
        self.tab = self.load()
        self.index = [0] * len(taille_tab)
        self.image = pygame.image.load('assets/' + dossier + '/' + n_image[0] + ".png")
        if self.is_resize:
            self.image = pygame.transform.scale(self.image, self.size[0])
        self.tab_delay = []
        for i in range(len(temps)):
            self.tab_delay.append(["False"] * temps[i])
            self.tab_delay[i].append("True")
        self.index_delay = [0] * len(temps)

    def animated(self, i):
        self.index_delay[i] += 1
        if self.tab_delay[i][self.index_delay[i]] == "True":
            self.index_delay[i] = 0
            if self.index[i] == len(self.tab[i]) - 1:
                if self.is_stop:
                    if self.is_remove:
                        self.group.remove(self)
                    return
                self.index[i] = 0

            else:
                self.index[i] += 1

            self.image = self.tab[i][self.index[i]]



    def load(self):
        images = []
        for i in range(len(self.t_b)):
            images.append([])
            path = f'assets/{self.dossier}/{self.n_image[i]}/{self.n_image[i]}'

            for y in range(1, self.t_b[i] + 1):
                if self.is_resize:
                    images[i].append(pygame.transform.scale(pygame.image.load(path + str(y) + ".png"), self.size[i]))
                else:
                    images[i].append(pygame.image.load(path + str(y) + ".png"))
        return images
