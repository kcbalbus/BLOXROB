import pygame
import constant_values

BOARD_X = constant_values.BOARD_X
BOARD_Y = constant_values.BOARD_Y

class Background():

    def __init__(self, difficulty):
        super().__init__()
        self.image = pygame.image.load(f'graphics/background_{difficulty}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 0))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
