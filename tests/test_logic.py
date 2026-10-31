"""Pure game movement checks."""

import copy

import logic


def test_new_game_has_two_tiles():
    board = logic.start_game()
    assert len(board) == 4
    assert all(len(row) == 4 for row in board)
    assert sum(tile != 0 for row in board for tile in row) == 2
    assert sum(tile for row in board for tile in row) == 4


def test_left_merges_correctly_and_scores():
    board = [
        [2, 2, 0, 0],
        [4, 4, 4, 4],
        [0, 0, 0, 0],
        [2, 0, 2, 0],
    ]
    original = copy.deepcopy(board)
    result, changed, score = logic.move_left(board)
    assert changed
    assert score == 24
    assert result[0] == [4, 0, 0, 0]
    assert result[1] == [8, 8, 0, 0]
    assert result[3] == [4, 0, 0, 0]
    assert board == original


def test_blocked_move_does_not_change_board():
    board = [
        [2, 4, 8, 16],
        [4, 8, 16, 32],
        [8, 16, 32, 64],
        [16, 32, 64, 128],
    ]
    result, changed, score = logic.move_left(board)
    assert result == board
    assert changed is False
    assert score == 0
    assert logic.get_current_state(board) == "KAYIP"
