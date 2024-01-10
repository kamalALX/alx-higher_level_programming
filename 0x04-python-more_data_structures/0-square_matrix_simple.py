#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = []
    for element in matrix:
        res = list(map(lambda x: x * x, element))
        copy_matrix.append(res)
    return copy_matrix
