import pygame

class Board(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/board.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 100))