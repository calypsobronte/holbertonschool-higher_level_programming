#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        new_matrix = []
        for i in matrix:
            new_matrix.append([j ** 2 for j in i])
        return new_matrix
