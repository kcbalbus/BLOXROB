import pygame
import constant_values
import abc

BOARD_X = constant_values.BOARD_X
BOARD_Y = constant_values.BOARD_Y
FONT = constant_values.FONT

class GUIElement(abc.ABC):

    def __init__(self):
        super().__init__()
        self.image = None
        self.rect = None

    def draw(self, screen):
        screen.blit(self.image, self.rect)



class Background(GUIElement):

    def __init__(self, difficulty):
        super().__init__()
        self.image = pygame.image.load(f'graphics/background_{difficulty}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 0))


class Board(GUIElement):

    def __init__(self, difficulty):
        super().__init__()
        self.image = pygame.image.load(f'graphics/board_{difficulty}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(BOARD_X, BOARD_Y))


class Button(GUIElement):

    def __init__(self, x, y, type, difficulty):
        super().__init__()
        self.image = pygame.image.load(f'graphics/button_{type}_{difficulty.lower()}.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

    def clicked(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            return True
        return False


class Text(GUIElement):

    def __init__(self, x, y, size, text):
        super().__init__()
        font = pygame.font.Font(FONT, size)
        self.image = font.render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
