import pygame

BLOCK_SIZE = 100
BOARD_X = 25
BOARD_Y = 125
BOARD_SIZE_X = 400
BOARD_SIZE_Y = 500

class Block(pygame.sprite.Sprite):
    WIDTH = 0
    HEIGHT = 0

    def __init__(self, x, y):
        super().__init__()
        self.x=x
        self.y=y
        self.image = None
        self.rect = None
        self.selected = False
        self.offset_x = 0
        self.offset_y = 0


    def prepare_rect(self):
        return self.image.get_rect(topleft = (BOARD_X+BLOCK_SIZE*self.x, BOARD_Y+BLOCK_SIZE*self.y))

    def update(self, mouse_pos):
        if self.selected:
            if pygame.mouse.get_pressed()[0]:  # Sprawdzenie, czy lewy przycisk myszy jest wciśnięty
                # Oblicz przesunięcie kursora
                mouse_x = mouse_pos[0]
                mouse_y = mouse_pos[1]

                top_left_x = self.rect.x
                top_left_y = self.rect.y
                bot_right_x = self.rect.x + self.WIDTH * BLOCK_SIZE
                bot_right_y = self.rect.y + self.HEIGHT * BLOCK_SIZE

                # Aktualizuj pozycję bloku z uwzględnieniem ograniczeń ruchu
                if top_left_y>mouse_y>BOARD_Y:
                    self.rect.y -= BLOCK_SIZE
                elif bot_right_y<mouse_y<BOARD_Y+BOARD_SIZE_Y:
                    self.rect.y += BLOCK_SIZE
                elif top_left_x>mouse_x>BOARD_X:
                    self.rect.x -= BLOCK_SIZE
                elif bot_right_x<mouse_x<BOARD_X+BOARD_SIZE_X:
                    self.rect.x += BLOCK_SIZE
            else:
                self.selected = False  # Zakończ przesuwanie bloku
        else:
            if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                self.selected = True
                self.click_pos = mouse_pos
                self.original_rect = self.rect.copy()


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