import pygame

class Block(pygame.sprite.Sprite):
    WIDTH = 1
    HEIGHT = 1

    def __init__(self, x, y):
        super().__init__()
        self.x=x
        self.y=y
        self.image = None
        self.rect = None


    def prepare_rect(self):
        return self.image.get_rect(topleft = (25+100*self.x, 125+100*self.y))


class Block1x1(Block):
    WIDTH=1
    HEIGHT=1
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image= pygame.image.load('graphics/block1x1.png').convert_alpha()
        self.rect = self.prepare_rect()


class Block2x1(Block):
    WIDTH=1
    HEIGHT=2
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('graphics/block2x1.png')
        self.rect = self.prepare_rect()


class Block1x2(Block):
    WIDTH=2
    HEIGHT=1
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('graphics/block1x2.png')
        self.rect = self.prepare_rect()


class Block2x2(Block):
    WIDTH=2
    HEIGHT=2
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('graphics/block2x2.png')
        self.rect = self.prepare_rect()