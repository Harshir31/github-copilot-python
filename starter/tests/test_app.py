import copy

import app as app_module


def test_index_renders_game_page(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Sudoku Game" in response.data


def test_new_game_returns_nine_by_nine_puzzle(client):
    response = client.get("/new?clues=40")
    puzzle = response.get_json()["puzzle"]

    assert response.status_code == 200
    assert len(puzzle) == 9
    assert all(len(row) == 9 for row in puzzle)
    assert all(cell in range(10) for row in puzzle for cell in row)


def test_check_without_game_returns_error(client):
    response = client.post("/check", json={"board": []})

    assert response.status_code == 400
    assert response.get_json() == {"error": "No game in progress"}


def test_check_accepts_the_generated_solution(client):
    client.get("/new")
    solution = copy.deepcopy(app_module.CURRENT["solution"])

    response = client.post("/check", json={"board": solution})

    assert response.status_code == 200
    assert response.get_json() == {"incorrect": []}


def test_check_reports_an_incorrect_cell(client):
    client.get("/new")
    board = copy.deepcopy(app_module.CURRENT["solution"])
    board[0][0] = board[0][0] % 9 + 1

    response = client.post("/check", json={"board": board})

    assert response.status_code == 200
    assert response.get_json() == {"incorrect": [[0, 0]]}
