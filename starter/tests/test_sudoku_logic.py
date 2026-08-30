import sudoku_logic


def test_create_empty_board_returns_nine_by_nine_zero_board():
    board = sudoku_logic.create_empty_board()

    assert len(board) == sudoku_logic.SIZE
    assert all(len(row) == sudoku_logic.SIZE for row in board)
    assert all(cell == sudoku_logic.EMPTY for row in board for cell in row)


def test_is_safe_rejects_row_column_and_box_conflicts():
    board = sudoku_logic.create_empty_board()
    board[0][0] = 5

    assert sudoku_logic.is_safe(board, 0, 1, 4)
    assert not sudoku_logic.is_safe(board, 0, 1, 5)
    assert not sudoku_logic.is_safe(board, 1, 0, 5)
    assert not sudoku_logic.is_safe(board, 1, 1, 5)


def test_find_incorrect_cells_returns_empty_for_matching_boards():
    solution = sudoku_logic.create_empty_board()

    assert sudoku_logic.find_incorrect_cells(solution, solution) == []


def test_find_incorrect_cells_returns_all_mismatched_coordinates():
    solution = sudoku_logic.create_empty_board()
    board = sudoku_logic.deep_copy(solution)
    board[0][1] = 1
    board[8][7] = 9

    assert sudoku_logic.find_incorrect_cells(board, solution) == [[0, 1], [8, 7]]


def test_fill_board_creates_a_valid_solution():
    board = sudoku_logic.create_empty_board()

    assert sudoku_logic.fill_board(board)
    assert all(cell in range(1, sudoku_logic.SIZE + 1) for row in board for cell in row)
    for row in range(sudoku_logic.SIZE):
        for col in range(sudoku_logic.SIZE):
            value = board[row][col]
            board[row][col] = sudoku_logic.EMPTY
            assert sudoku_logic.is_safe(board, row, col, value)
            board[row][col] = value


def test_count_solutions_returns_one_for_a_completed_board_without_mutating_it():
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]
    original = sudoku_logic.deep_copy(board)

    assert sudoku_logic.count_solutions(board) == 1
    assert board == original


def test_count_solutions_stops_at_two_for_an_empty_board():
    board = sudoku_logic.create_empty_board()
    original = sudoku_logic.deep_copy(board)

    assert sudoku_logic.count_solutions(board) == 2
    assert board == original


def test_count_solutions_returns_zero_for_an_invalid_board():
    board = sudoku_logic.create_empty_board()
    board[0][0] = 5
    board[0][1] = 5

    assert sudoku_logic.count_solutions(board) == 0


def test_count_solutions_returns_zero_for_duplicate_in_column():
    board = sudoku_logic.create_empty_board()
    board[0][0] = 5
    board[1][0] = 5

    assert sudoku_logic.count_solutions(board) == 0


def test_count_solutions_returns_zero_for_duplicate_in_box():
    board = sudoku_logic.create_empty_board()
    board[0][0] = 5
    board[1][1] = 5

    assert sudoku_logic.count_solutions(board) == 0


def test_generate_puzzle_returns_default_clue_count_and_solution():
    puzzle, solution = sudoku_logic.generate_puzzle()

    assert len(puzzle) == sudoku_logic.SIZE
    assert len(solution) == sudoku_logic.SIZE
    assert sum(cell != sudoku_logic.EMPTY for row in puzzle for cell in row) == 35
    assert all(
        cell in range(1, sudoku_logic.SIZE + 1)
        for row in solution
        for cell in row
    )
    assert all(
        puzzle[row][col] in (sudoku_logic.EMPTY, solution[row][col])
        for row in range(sudoku_logic.SIZE)
        for col in range(sudoku_logic.SIZE)
    )
    assert sudoku_logic.count_solutions(puzzle) == 1
