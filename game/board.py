import pygame

class Board(pygame.sprite.Sprite):

    def __init__(self, difficulty):
        super().__init__()
        self.image = pygame.image.load(f'graphics/board_{difficulty}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 100))