import pygame
import sys
from pieces import *
from GUI_elements import *
from game_data import GameData
import constant_values

pygame.init()

WIDTH = constant_values.WIDTH
HEIGHT = constant_values.HEIGHT

FONT = constant_values.FONT


# Utworzenie okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GTA VI")
clock = pygame.time.Clock()
game_data = GameData()

def lvl_setup(difficulty):
    return game_data.load_lvl(difficulty)

def lvl_restart(difficulty):
    return game_data.restart_lvl(difficulty)

def restart_lvl_state(difficulty):
    game_data.restart_lvl_state(difficulty)

def lvl_save(difficulty, blocks_group, moves):
    game_data.save_lvl(difficulty, blocks_group, moves)


def check_move(blocks_group):
    moved = False
    for block in blocks_group:
        if block.move == "just_moved":
            moved = True
            block.reset_moved()

    return moved

def create_blocks_group(blocks_setup):
    # Grupa sprite'ów, w której przechowujemy klocki
    blocks_group = pygame.sprite.Group()
    for block in blocks_setup:
        blocks_group.add(block)

    return blocks_group


def display_moves(moves, screen):
    curr_score = Text(110, 110, 22, str(moves))
    curr_score.draw(screen)


def save_score(difficulty, moves):
    return game_data.save_best_score(difficulty, moves)

def get_best_score(difficulty):
    best_scores = game_data.load_best_scores()

    return best_scores[difficulty]

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

    background = Background("menu")
    button_easy = Button(0, 200, "menu", "easy")
    button_medium = Button(0, 300, "menu", "medium")
    button_hard = Button(0, 400, "menu", "hard")
    button_help = Button(0, 500, "menu", "help")
    button_quit = Button(0, 600, "menu", "quit")

    game_data.load_data()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_easy.clicked(mouse_pos):
                    start_game("Easy")
                elif button_medium.clicked(mouse_pos):
                    start_game("Medium")
                elif button_hard.clicked(mouse_pos):
                    start_game("Hard")
                elif button_help.clicked(mouse_pos):
                    show_rules()
                elif button_quit.clicked(mouse_pos):
                    quit_game()

        background.draw(screen)
        button_easy.draw(screen)
        button_medium.draw(screen)
        button_hard.draw(screen)
        button_help.draw(screen)
        button_quit.draw(screen)

        pygame.display.flip()
        clock.tick(60)


def start_game(difficulty):
    # Tutaj możesz dodać kod do rozpoczęcia gry z wybranym poziomem trudności
    print("Rozpoczęto nową grę - poziom trudności:", difficulty)
    BUTTON_HOUSE_X = constant_values.BUTTON_HOUSE_X
    BUTTON_HOUSE_Y = constant_values.BUTTON_HOUSE_Y
    BUTTON_RETRY_X = constant_values.BUTTON_RETRY_X
    BUTTON_RETRY_Y = constant_values.BUTTON_RETRY_Y

    font = pygame.font.Font(None, 30)

    background = Background(difficulty)
    board = Board(difficulty)

    button_house = Button(BUTTON_HOUSE_X, BUTTON_HOUSE_Y, "house", difficulty)
    button_retry = Button(BUTTON_RETRY_X, BUTTON_RETRY_Y, "retry", difficulty)
    button_list = [button_house, button_retry]

    best_score = Text(187, 64, 22, str(get_best_score(difficulty)))

    blocks_setup, moves = lvl_setup(difficulty)
    blocks_group = create_blocks_group(blocks_setup)


    # Główna pętla gry
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvl_save(difficulty, blocks_group.sprites(), moves)
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
               if button_retry.clicked(mouse_pos):
                    blocks_setup, moves = lvl_restart(difficulty)
                    blocks_group = create_blocks_group(blocks_setup)
               elif button_house.clicked(mouse_pos):
                    lvl_save(difficulty, blocks_group.sprites(), moves)
                    running = False


        background.draw(screen)
        button_retry.draw(screen)
        button_house.draw(screen)
        best_score.draw(screen)
        board.draw(screen)
        blocks_group.draw(screen)
        blocks_group.update(mouse_pos, blocks_group)

        if check_move(blocks_group):
            moves+=1

        display_moves(moves, screen)

        if blocks_group.sprites()[-1].check_win_condition():
            print("Poziom ukończony")
            running=lvl_completed(difficulty, moves)
            blocks_setup, moves = lvl_restart(difficulty)
            blocks_group = create_blocks_group(blocks_setup)


        pygame.display.flip()
        clock.tick(60)


def lvl_completed(difficulty, moves):
    is_best_score = save_score(difficulty, moves)
    print(is_best_score)

    font = pygame.font.Font(None, 50)

    completed_text = font.render(f"Level {difficulty} completed!", True, (0, 0, 0))
    score_text = font.render(f"Moves: {moves}", True, (0, 0, 0))
    if is_best_score:
        best_score_text = font.render("New best score!", True, (0, 0, 0))
    else:
        best_score_text = font.render(f"Best score: {get_best_score(difficulty)}", True, (0, 0, 0))
    return_to_menu_text = font.render("Return To Main Menu", True, (0, 0, 0))
    restart_lvl_text = font.render("Restart Level", True, (0, 0, 0))

    completed_rect = completed_text.get_rect(center = (WIDTH/2, 100))
    score_rect = score_text.get_rect(center = (WIDTH/2, 200))
    best_score_rect = best_score_text.get_rect(center = (WIDTH/2, 300))
    return_to_menu_rect = return_to_menu_text.get_rect(topright = (WIDTH/2-50, 400))
    restart_lvl_rect = restart_lvl_text.get_rect(topleft = (WIDTH/2+100, 400))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if restart_lvl_rect.collidepoint(mouse_pos):
                    return True
                elif return_to_menu_rect.collidepoint(mouse_pos):
                    restart_lvl_state(difficulty)
                    return False

        screen.fill((100, 100, 100))
        screen.blit(completed_text, completed_rect)
        screen.blit(score_text, score_rect)
        screen.blit(best_score_text, best_score_rect)
        screen.blit(return_to_menu_text, return_to_menu_rect)
        screen.blit(restart_lvl_text, restart_lvl_rect)

        pygame.display.flip()
        clock.tick(60)






if __name__ == "__main__":
    # Uruchomienie gry
    create_main_menu()
