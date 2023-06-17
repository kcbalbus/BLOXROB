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
        self.image = None
        self.rect = None
        self.selected = False
        self.offset_x = 0
        self.offset_y = 0


    def prepare_rect(self, x, y):
        return self.image.get_rect(topleft = (BOARD_X+BLOCK_SIZE*x, BOARD_Y+BLOCK_SIZE*y))

    def update(self, mouse_pos, blocks_group):
        if self.selected:
            if pygame.mouse.get_pressed()[0]:  # Sprawdzenie, czy lewy przycisk myszy jest wciśnięty

                move = self.move_block(mouse_pos[0], mouse_pos[1])

                self.check_collisions(blocks_group, move)

            else:
                self.selected = False  # Zakończ przesuwanie bloku
        else:
            if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0] and self.check_move_slot(blocks_group):
                self.selected = True

    def move_block(self, mouse_x, mouse_y):
        top_left_x = self.rect.x
        top_left_y = self.rect.y
        bot_right_x = self.rect.x + self.WIDTH * BLOCK_SIZE
        bot_right_y = self.rect.y + self.HEIGHT * BLOCK_SIZE

        move = None

        # Aktualizuj pozycję bloku z uwzględnieniem ograniczeń ruchu
        if top_left_y > mouse_y > BOARD_Y:
            move = "up"
            self.move_block_up()
        elif bot_right_y < mouse_y < BOARD_Y + BOARD_SIZE_Y:
            move = "down"
            self.move_block_down()
        elif top_left_x > mouse_x > BOARD_X:
            move = "left"
            self.move_block_left()
        elif bot_right_x < mouse_x < BOARD_X + BOARD_SIZE_X:
            move = "right"
            self.move_block_right()

        return move

    def move_block_up(self):
        self.rect.y -= BLOCK_SIZE
    def move_block_down(self):
        self.rect.y += BLOCK_SIZE

    def move_block_left(self):
        self.rect.x -= BLOCK_SIZE

    def move_block_right(self):
        self.rect.x += BLOCK_SIZE


    def check_move_slot(self, blocks_group):
        for block in blocks_group:
            if block.selected:
                return False

        return True

    def check_collisions(self, blocks_group, move):
        if move is not None:
            colliding_blocks = pygame.sprite.spritecollide(self, blocks_group, False)
            if len(colliding_blocks) > 1:
                if move == "up":
                    self.move_block_down()
                elif move == "down":
                    self.move_block_up()
                elif move == "left":
                    self.move_block_right()
                elif move == "right":
                    self.move_block_left()


    def getX(self):
        return (self.rect.x-BOARD_X)/BLOCK_SIZE

    def getY(self):
        return (self.rect.y-BOARD_Y)/BLOCK_SIZE


class Block1x1(Block):
    WIDTH=1
    HEIGHT=1
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image= pygame.image.load('graphics/block1x1.png').convert_alpha()
        self.rect = self.prepare_rect(x, y)


class Block2x1(Block):
    WIDTH=1
    HEIGHT=2
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('graphics/block2x1.png')
        self.rect = self.prepare_rect(x, y)


class Block1x2(Block):
    WIDTH=2
    HEIGHT=1
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('graphics/block1x2.png')
        self.rect = self.prepare_rect(x, y)


class Block2x2(Block):
    WIDTH=2
    HEIGHT=2
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load('graphics/block2x2.png')
        self.rect = self.prepare_rect(x, y)

    def check_win_condition(self):
        # Sprawdź, czy klocek 2x2 znajduje się na środku dolnego rzędu planszy
        if self.rect.x == BOARD_X + 1 * BLOCK_SIZE and self.rect.y == BOARD_Y + 3 * BLOCK_SIZE:
            return True
        else:
            return False