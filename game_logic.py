import random
import pygame
import math

from main_functions import *
from minimax import minimax
from alpha_beta_pruning import alpha_beta


def draw_board(board, screen):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (
            int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, YELLOW, (
                int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
    pygame.display.update()


def minimax_game(depth):
    board = create_board()
    board = board.astype(int)
    print_board(board)

    screen = pygame.display.set_mode(size)

    pygame.init()

    draw_board(board, screen)
    pygame.display.update()

    turn = random.randint(PLAYER, AI)

    font = pygame.font.SysFont("monospace", 75)

    tie_counter = 0
    exit_flag = False
    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                exit_flag = True
                break

            if event.type == pygame.KEYDOWN:
                # Player turn

                if turn == PLAYER:
                    col = minimax(board, 1, False)[0]
                    # col = random.randint(0,6)

                    if is_valid_location(board, col).all():
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_PIECE)

                        if winning_move(board, PLAYER_PIECE):
                            label = font.render("Computer wins!!", True, RED)
                            screen.blit(label, (40, 10))
                            pygame.display.update()
                            game_over = True

                        turn += 1
                        turn = turn % 2
                        tie_counter += 1

                        print_board(board)
                        draw_board(board, screen)

        # AI Turn
        if turn == AI and not game_over:

            col = minimax(board, depth, True)[0]

            if is_valid_location(board, col).all():
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = font.render("AI Agent wins!!", True, YELLOW)
                    screen.blit(label, (40, 10))
                    pygame.display.update()
                    game_over = True

                print_board(board)
                draw_board(board, screen)

                turn += 1
                turn = turn % 2
                tie_counter += 1

        if tie_counter == COLUMN_COUNT*ROW_COUNT:
            label = font.render("Tie game!", True, BLUE)
            screen.blit(label, (120, 10))
            pygame.display.update()
            game_over = True

            if game_over and exit_flag:
                break

    while not exit_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = True


def alpha_bete_game(depth):
    board = create_board()
    board = board.astype(int)
    print_board(board)

    screen = pygame.display.set_mode(size)

    pygame.init()

    draw_board(board, screen)
    pygame.display.update()

    turn = random.randint(PLAYER, AI)

    font = pygame.font.SysFont("monospace", 75)

    tie_counter = 0
    exit_flag = False
    game_over = False
    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                exit_flag = True
                break

            if event.type == pygame.KEYDOWN:
                # Player turn

                if turn == PLAYER:
                    col = minimax(board, 1, False)[0]
                    # col = random.randint(0,6)

                    if is_valid_location(board, col).any():
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, PLAYER_PIECE)

                        if winning_move(board, PLAYER_PIECE):
                            label = font.render("Computer wins!!", True, RED)
                            screen.blit(label, (40, 10))
                            pygame.display.update()
                            game_over = True

                        turn += 1
                        turn = turn % 2
                        tie_counter += 1

                        print_board(board)
                        draw_board(board, screen)

        # AI Turn
        if turn == AI and not game_over:

            col = alpha_beta(board, depth, -math.inf, math.inf, True)[0]

            if is_valid_location(board, col).all():
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)

                if winning_move(board, AI_PIECE):
                    label = font.render("AI Agent wins!!", True, YELLOW)
                    screen.blit(label, (40, 10))
                    pygame.display.update()
                    game_over = True

                print_board(board)
                draw_board(board, screen)

                turn += 1
                turn = turn % 2
                tie_counter += 1

        if tie_counter == COLUMN_COUNT * ROW_COUNT:
            label = font.render("Tie game!", True, BLUE)
            screen.blit(label, (120, 10))
            pygame.display.update()
            game_over = True

        if game_over and exit_flag:
            break

    while not exit_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_flag = True
