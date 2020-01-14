#!/usr/bin/python3
def matrix_divided(matrix, div):
    m1 = "matrix must be a matrix (list of lists) of integers/floats"
    m2 = "Each row of the matrix must have the same size"
    m3 = "division by zero"
    m4 = "div must be a number"
    size = 0
    if div == 0:
        raise ZeroDivisionError(m3)

    if not isinstance(div, (int, float)):
        raise TypeError(m4)

    if not matrix or not isinstance(matrix, list):
        raise TypeError(m1)

    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(m1)

    if size != 0 and len(elements) != size:
        raise TypeError(m2)

    for num in elements:
        if not isinstance(num, (int, float)):
            raise TypeError(m1)

    size = len(elements)

    mat = [[round((f[i]/div), 2) for i in range(len(f))] for f in matrix]

    return mat
