import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, dir, path, animation_speed, default_mode, size=None, is_stop=False, group=None):
        super().__init__()
        self.dir = dir  # main dir
        self.path = path  # dict as {"under_dir": number_files}
        self.mode = default_mode  # idle, jump, run, etc. MUST be the name of an under dir
        self.animation_speed = animation_speed
        self.image_index = animation_speed
        self.is_stop = is_stop
        self.group = group

        self.images = self.load(size)  # dict as {"mode": [pygame_surface_images]}
        self.image = self.images[self.mode][0]

    def animated(self):
        self.image = self.images[self.mode][int(self.image_index)]

        if int(self.image_index + self.animation_speed) >= len(self.images[self.mode]):
            if not self.is_stop:
                self.image_index = 0
            else:
                if self.group is not None:
                    self.group.remove(self)

        else:
            self.image_index += self.animation_speed

    def load(self, size=None):
        images = {}
        for under_dir in self.path:
            temp = []
            for i in range(self.path[under_dir]):
                img = pygame.image.load(f"assets/{self.dir}/{under_dir}/{under_dir}{i + 1}.png")
                if size is not None:
                    img = pygame.transform.scale(img, size)
                temp.append(img)
            images[under_dir] = temp

        return images
