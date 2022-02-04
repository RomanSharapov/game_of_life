#!/usr/bin/env python3

# According to Wikipedia's article:
# "The Game of Life, also known simply as Life, is a cellular automaton devised by
# the British mathematician John Horton Conway in 1970."

# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or
# dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the
# following four rules (taken from the above Wikipedia article):
# 1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by over-population.
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

# The next state is created by applying the above rules simultaneously to every cell in the current state, where births
# and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


def print_board(board: list[list[int]]) -> None:
    """The board pretty print"""
    for _ in board:
        print(_)


def next_generation(board: list[list[int]]) -> list[list[int]]:
    m, n = len(board[0]), len(board)
    next_gen = [[None] * m for _ in range(n)]

    nb_pos = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

    for r, row in enumerate(board):
        for c, col in enumerate(row):
            nb_count = 0
            for i, j in nb_pos:
                if 0<=r+i<n and 0<=c+j<m:
                    nb_count += board[r+i][c+j]
            if col == 1:
                if nb_count < 2 or nb_count > 3:
                    next_gen[r][c] = 0
                elif nb_count in (2, 3):
                    next_gen[r][c] = 1
            if col == 0:
                next_gen[r][c] = 1 if nb_count == 3 else 0

    return next_gen


def play_game_of_life(board, max_generations=10, current_generation=1):
    print(f"generation {current_generation}")
    print_board(board)
    max_generations -= 1
    current_generation += 1
    if max_generations > 0:
        play_game_of_life(next_generation(board), max_generations, current_generation)
    else:
        print("End of Life")


if __name__ == "__main__":
    glider = [
        [0,1,0],
        [0,0,1],
        [1,1,1],
        [0,0,0],
    ]

    bliper = [
        [0,0,0],
        [1,1,1],
        [0,0,0],
    ]

    play_game_of_life(board=bliper, max_generations=2)
