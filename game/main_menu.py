import os
import pygame
import sys
from pieces import *
from GUI_elements import *
from game_data import GameData
import constant_values

WIDTH = constant_values.WIDTH
HEIGHT = constant_values.HEIGHT
FONT = constant_values.FONT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLOXROB")
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
    blocks_group = pygame.sprite.Group()
    for block in blocks_setup:
        blocks_group.add(block)

    return blocks_group


def display_moves_lvl(moves, screen):
    curr_score = Text(10, 110, 22, f"Moves: {moves}")
    curr_score.draw(screen)

def save_score(difficulty, moves):
    return game_data.save_best_score(difficulty, moves)

def draw_list(list):
    for item in list:
        item.draw(screen)

def get_best_score(difficulty):
    best_scores = game_data.load_best_scores()

    return best_scores[difficulty]

def create_main_menu():

    background = Background("menu")
    button_easy = Button(0, 200, "menu", "easy")
    button_medium = Button(0, 300, "menu", "medium")
    button_hard = Button(0, 400, "menu", "hard")
    button_help = Button(0, 500, "menu", "help")
    button_quit = Button(0, 600, "menu", "quit")

    to_draw_list = [background, button_easy, button_medium, button_hard, button_help, button_quit]

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

        draw_list(to_draw_list)

        pygame.display.flip()
        clock.tick(60)


def start_game(difficulty):
    BUTTON_HOUSE_X = constant_values.BUTTON_HOUSE_X
    BUTTON_HOUSE_Y = constant_values.BUTTON_HOUSE_Y
    BUTTON_RETRY_X = constant_values.BUTTON_RETRY_X
    BUTTON_RETRY_Y = constant_values.BUTTON_RETRY_Y

    background = Background(difficulty)
    board = Board(difficulty)
    button_house = Button(BUTTON_HOUSE_X, BUTTON_HOUSE_Y, "house", difficulty)
    button_retry = Button(BUTTON_RETRY_X, BUTTON_RETRY_Y, "retry", difficulty)
    best_score = Text(10, 65, 22, f"Best score: {get_best_score(difficulty)}")
    blocks_setup, moves = lvl_setup(difficulty)
    blocks_group = create_blocks_group(blocks_setup)

    to_draw_list=[background, board, button_house, button_retry, best_score, blocks_group]

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
                    to_draw_list[-1]=blocks_group
               elif button_house.clicked(mouse_pos):
                    lvl_save(difficulty, blocks_group.sprites(), moves)
                    running = False


        draw_list(to_draw_list)

        blocks_group.update(mouse_pos, blocks_group)

        if check_move(blocks_group):
            moves+=1

        display_moves_lvl(moves, screen)

        if blocks_group.sprites()[-1].check_win_condition():
            running=lvl_completed(difficulty, moves)
            best_score = Text(10, 65, 22, f"Best score: {get_best_score(difficulty)}")
            blocks_setup, moves = lvl_restart(difficulty)
            blocks_group = create_blocks_group(blocks_setup)
            to_draw_list[-1]=blocks_group
            to_draw_list[-2] = best_score


        pygame.display.flip()
        clock.tick(60)


def lvl_completed(difficulty, moves):
    is_best_score = save_score(difficulty, moves)
    restart_lvl_state(difficulty)


    if difficulty=="Medium":
        completed_font = 28
    else:
        completed_font = 31

    background = Background(f"completed_{difficulty}")
    completed = Text(20, 135, completed_font, f"{difficulty.upper()} - COMPLETED")
    score = Text(50, 265, 30, f"Moves: {moves}")
    if is_best_score:
        best_score = Text(45, 345, 30, "New best score!")
    else:
        best_score = Text(50, 345, 30, f"Best score: {get_best_score(difficulty)}")
    button_house = Button(0, 0, "house", difficulty)
    button_house.scale_and_change_position(150, 150, 255, 450)
    button_retry = Button(0, 0, "retry", difficulty)
    button_retry.scale_and_change_position(150, 150, 46, 450)

    to_draw_list = [background, completed, score, best_score, button_house, button_retry]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_retry.clicked(mouse_pos):
                    return True
                elif button_house.clicked(mouse_pos):
                    return False

        draw_list(to_draw_list)

        pygame.display.flip()
        clock.tick(60)


def show_rules():

    background = Background("help")
    button_house = Button(0, 0, "house", "help")
    button_house.scale_and_change_position(100, 100, 175, 570)

    to_draw_list = [background, button_house]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_house.clicked(mouse_pos):
                    running=False


        draw_list(to_draw_list)

        pygame.display.flip()
        clock.tick(60)

def quit_game():
    game_data.save_data()
    pygame.quit()
    sys.exit()




