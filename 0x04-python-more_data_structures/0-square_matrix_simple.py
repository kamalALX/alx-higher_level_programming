#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = list(map(list, matrix))
    i, j = 0, 0
    for i in range(len(matrix[i])):
        for j in range(len(matrix[j])):
            matrix_copy[i][j] **= 2
    return matrix_copy
