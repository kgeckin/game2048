# logic.py
import random

def start_game():
    mat = [[0] * 4 for _ in range(4)]
    add_new_2(mat)
    add_new_2(mat)
    return mat

def add_new_2(mat):
    empty_cells = [(i, j) for i in range(4) for j in range(4) if mat[i][j] == 0]
    if not empty_cells:
        return
    i, j = random.choice(empty_cells)
    mat[i][j] = 2

def get_current_state(mat):
    # Kazanma kontrolü
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'KAZANDI'
    # Boş hücre varsa
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'OYUN BİTMEDİ'
    # Yatay birleşme kontrolü
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1]:
                return 'OYUN BİTMEDİ'
    # Dikey birleşme kontrolü
    for j in range(4):
        for i in range(3):
            if mat[i][j] == mat[i+1][j]:
                return 'OYUN BİTMEDİ'
    return 'KAYIP'

def compress(mat):
    new_mat = [[0] * 4 for _ in range(4)]
    changed = False
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_mat, changed

def merge(mat):
    changed = False
    score_inc = 0
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                score_inc += mat[i][j]
                mat[i][j+1] = 0
                changed = True
    return mat, changed, score_inc

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append(mat[i][::-1])
    return new_mat

def transpose(mat):
    new_mat = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            new_mat[i][j] = mat[j][i]
    return new_mat

def move_left(mat):
    new_mat, changed1 = compress(mat)
    new_mat, changed2, score_inc = merge(new_mat)
    changed = changed1 or changed2
    new_mat, _ = compress(new_mat)
    return new_mat, changed, score_inc

def move_right(mat):
    reversed_mat = reverse(mat)
    new_mat, changed, score_inc = move_left(reversed_mat)
    final_mat = reverse(new_mat)
    return final_mat, changed, score_inc

def move_up(mat):
    transposed_mat = transpose(mat)
    new_mat, changed, score_inc = move_left(transposed_mat)
    final_mat = transpose(new_mat)
    return final_mat, changed, score_inc

def move_down(mat):
    transposed_mat = transpose(mat)
    new_mat, changed, score_inc = move_right(transposed_mat)
    final_mat = transpose(new_mat)
    return final_mat, changed, score_inc
