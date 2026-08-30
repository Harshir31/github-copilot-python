import copy
import random

SIZE = 9
EMPTY = 0
MAX_SOLUTIONS = 2

def deep_copy(board):
    return copy.deepcopy(board)

def create_empty_board():
    return [[EMPTY for _ in range(SIZE)] for _ in range(SIZE)]

def is_safe(board, row, col, num):
    # Check row and column
    for x in range(SIZE):
        if board[row][x] == num or board[x][col] == num:
            return False
    # Check 3x3 box
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def fill_board(board):
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] == EMPTY:
                possible = list(range(1, SIZE + 1))
                random.shuffle(possible)
                for candidate in possible:
                    if is_safe(board, row, col, candidate):
                        board[row][col] = candidate
                        if fill_board(board):
                            return True
                        board[row][col] = EMPTY
                return False
    return True

def _has_valid_entries(board):
    for row in range(SIZE):
        for col in range(SIZE):
            value = board[row][col]
            if value == EMPTY:
                continue
            board[row][col] = EMPTY
            valid = is_safe(board, row, col, value)
            board[row][col] = value
            if not valid:
                return False
    return True

def count_solutions(board):
    if len(board) != SIZE or any(len(row) != SIZE for row in board):
        return 0
    if any(
        not isinstance(cell, int) or cell < EMPTY or cell > SIZE
        for row in board
        for cell in row
    ):
        return 0
    if not _has_valid_entries(board):
        return 0

    solution_count = 0

    def search():
        nonlocal solution_count
        if solution_count >= MAX_SOLUTIONS:
            return

        best_cell = None
        best_candidates = None
        for row in range(SIZE):
            for col in range(SIZE):
                if board[row][col] == EMPTY:
                    candidates = [
                        number
                        for number in range(1, SIZE + 1)
                        if is_safe(board, row, col, number)
                    ]
                    if not candidates:
                        return
                    if best_candidates is None or len(candidates) < len(best_candidates):
                        best_cell = (row, col)
                        best_candidates = candidates
                        if len(candidates) == 1:
                            break
            if best_candidates is not None and len(best_candidates) == 1:
                break

        if best_cell is None:
            solution_count += 1
            return

        row, col = best_cell
        for candidate in best_candidates:
            board[row][col] = candidate
            search()
            board[row][col] = EMPTY
            if solution_count >= MAX_SOLUTIONS:
                return

    search()
    return solution_count

def remove_cells(board, clues):
    if not 0 <= clues <= SIZE * SIZE:
        raise ValueError("clues must be between 0 and 81")

    coordinates = [(row, col) for row in range(SIZE) for col in range(SIZE)]
    random.shuffle(coordinates)
    for row, col in coordinates:
        if sum(cell != EMPTY for current_row in board for cell in current_row) <= clues:
            return
        value = board[row][col]
        if board[row][col] != EMPTY:
            board[row][col] = EMPTY
            if count_solutions(board) != 1:
                board[row][col] = value

    if sum(cell != EMPTY for row in board for cell in row) > clues:
        raise ValueError("could not generate a uniquely solvable puzzle with this clue count")

def find_incorrect_cells(board, solution):
    incorrect = []
    for row in range(SIZE):
        for col in range(SIZE):
            if board[row][col] != solution[row][col]:
                incorrect.append([row, col])
    return incorrect

def generate_puzzle(clues=35):
    board = create_empty_board()
    fill_board(board)
    solution = deep_copy(board)
    remove_cells(board, clues)
    puzzle = deep_copy(board)
    return puzzle, solution
