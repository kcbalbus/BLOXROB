import pygame
import sys
from pieces import *
from board import *

pygame.init()


# Ustawienia ekranu
WIDTH = 450
HEIGHT = 700
BG_COLOR = (255, 255, 255)

# Utworzenie okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Klotski Game")
clock = pygame.time.Clock()

# Funkcje układające bloki w zależności od poziomu gry
def setup_easy():
    raise NotImplemented

def setup_medium():
    block_2x1_1 = Block2x1(0, 0)
    block_2x1_2 = Block2x1(3, 0)
    block_2x1_3 = Block2x1(0, 3)
    block_2x1_4 = Block2x1(3, 3)
    block_1x1_1 = Block1x1(0, 2)
    block_1x1_2 = Block1x1(3, 2)
    block_1x1_3 = Block1x1(1, 3)
    block_1x1_4 = Block1x1(2, 3)
    block_1x1_5 = Block1x1(1, 4)
    block_1x1_6 = Block1x1(2, 4)
    block_2x2_1 = Block2x2(1, 0)

    return [block_2x1_1, block_2x1_2, block_2x1_3, block_2x1_4, block_1x1_1, block_1x1_2, block_1x1_3, block_1x1_4,
            block_1x1_5, block_1x1_6, block_2x2_1]

def setup_hard():
    raise NotImplemented

# Funkcja do rozpoczęcia nowej gry
def start_game(difficulty):
    # Tutaj możesz dodać kod do rozpoczęcia gry z wybranym poziomem trudności
    print("Rozpoczęto nową grę - poziom trudności:", difficulty)

    blocks_setup = None

    if difficulty == "Easy":
        blocks_setup=setup_easy()
    elif difficulty == "Medium":
        blocks_setup=setup_medium()
    else:
        blocks_setup = setup_hard()

    board = Board()

    board_group = pygame.sprite.GroupSingle()
    board_group.add(board)

    # Grupa sprite'ów, w której przechowujemy klocki
    blocks_group = pygame.sprite.Group()
    for block in blocks_setup:
        blocks_group.add(block)


    block_move_slot_available = False

    # Główna pętla gry
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        mouse_pos = pygame.mouse.get_pos()

        screen.fill((100, 100, 100))
        board_group.draw(screen)
        blocks_group.draw(screen)

        mouse_pressed = pygame.mouse.get_pressed()

        if mouse_pressed[0] and not block_move_slot_available:
            blocks_group.update(mouse_pos, blocks_group, True)
        else:
            blocks_group.update(mouse_pos, blocks_group, False)

        block_move_slot_available = mouse_pressed[0]

        pygame.display.flip()
        clock.tick(60)


# Funkcja do wyświetlania zasad gry
def show_rules():
    # Tutaj możesz dodać kod do wyświetlenia zasad gry
    print("Zasady gry")

# Funkcja do zakończenia gry
def quit_game():
    pygame.quit()
    sys.exit()

# Tworzenie menu głównego
def create_main_menu():
    font = pygame.font.Font(None, 50)
    title_text = font.render("Klotski Game", True, (0, 0, 0))
    easy_text = font.render("Easy", True, (0, 0, 0))
    medium_text = font.render("Medium", True, (0, 0, 0))
    hard_text = font.render("Hard", True, (0, 0, 0))
    rules_text = font.render("Rules", True, (0, 0, 0))
    quit_text = font.render("Quit", True, (0, 0, 0))

    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
    easy_rect = easy_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    medium_rect = medium_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    hard_rect = hard_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
    rules_rect = rules_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))
    quit_rect = quit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if easy_rect.collidepoint(mouse_pos):
                    start_game("Easy")
                elif medium_rect.collidepoint(mouse_pos):
                    start_game("Medium")
                elif hard_rect.collidepoint(mouse_pos):
                    start_game("Hard")
                elif rules_rect.collidepoint(mouse_pos):
                    show_rules()
                elif quit_rect.collidepoint(mouse_pos):
                    quit_game()

        screen.fill((100, 100, 100))
        screen.blit(title_text, title_rect)
        screen.blit(easy_text, easy_rect)
        screen.blit(medium_text, medium_rect)
        screen.blit(hard_text, hard_rect)
        screen.blit(rules_text, rules_rect)
        screen.blit(quit_text, quit_rect)

        pygame.display.flip()
        clock.tick(60)

# Uruchomienie gry
create_main_menu()