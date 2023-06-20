import pygame
import constant_values

BOARD_X = constant_values.BOARD_X
BOARD_Y = constant_values.BOARD_Y

class Button():

    def __init__(self, x, y, type, difficulty):
        super().__init__()
        self.image = pygame.image.load(f'graphics/button_{type}_{difficulty.lower()}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen, mouse_pos):
        screen.blit(self.image, self.rect)

    def clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False
