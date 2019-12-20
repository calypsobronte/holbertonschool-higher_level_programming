#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda n1: list(map(lambda n2: n2 ** 2, n1)), matrix))
