import pygame
import sys
from pieces import *
from board import *
from game_data import GameData

pygame.init()


# Ustawienia ekranu
WIDTH = 450
HEIGHT = 700
BG_COLOR = (255, 255, 255)

# Utworzenie okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GTA VI")
clock = pygame.time.Clock()
game_data = GameData()

def lvl_setup(difficulty):
    return game_data.load_lvl(difficulty)

def lvl_restart(difficulty):
    return game_data.restart_lvl(difficulty)

def lvl_save(difficulty, blocks_group, moves):
    game_data.save_lvl(difficulty, blocks_group, moves)



# Funkcja do rozpoczęcia nowej gry
def start_game(difficulty):
    # Tutaj możesz dodać kod do rozpoczęcia gry z wybranym poziomem trudności
    print("Rozpoczęto nową grę - poziom trudności:", difficulty)

    blocks_setup, moves = lvl_setup(difficulty)


    board = Board()

    board_group = pygame.sprite.GroupSingle()
    board_group.add(board)

    # Grupa sprite'ów, w której przechowujemy klocki
    blocks_group = pygame.sprite.Group()
    for block in blocks_setup:
        blocks_group.add(block)


    # Główna pętla gry
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvl_save(difficulty, blocks_group.sprites(), moves)
                running = False

        mouse_pos = pygame.mouse.get_pos()

        screen.fill((100, 100, 100))
        board_group.draw(screen)
        blocks_group.draw(screen)
        blocks_group.update(mouse_pos, blocks_group)


        if blocks_group.sprites()[-1].check_win_condition():
            print("Poziom ukończony")
            running = False

        pygame.display.flip()
        clock.tick(60)


# Funkcja do wyświetlania zasad gry
def show_rules():
    # Tutaj możesz dodać kod do wyświetlenia zasad gry
    print("Zasady gry")

# Funkcja do zakończenia gry
def quit_game():
    game_data.save_data()
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

    game_data.load_data()

    print(game_data.game_data)

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

if __name__ == "__main__":
    # Uruchomienie gry
    create_main_menu()
