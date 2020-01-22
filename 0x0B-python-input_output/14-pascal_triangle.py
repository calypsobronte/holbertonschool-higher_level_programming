#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    array = []
    array.append([1, ])
    for i in range(0, n - 1):
        array_size = [1, ]
        for j in range(0, len(array[-1]) - 1):
            array_size.append(array[-1][j] + array[-1][j + 1])
        array_size.append(1)
        array.append(array_size)
    return array