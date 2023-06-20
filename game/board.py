import pygame
import constant_values

BOARD_X = constant_values.BOARD_X
BOARD_Y = constant_values.BOARD_Y

class Board():

    def __init__(self, difficulty):
        super().__init__()
        self.image = pygame.image.load(f'graphics/board_{difficulty}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(BOARD_X, BOARD_Y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)