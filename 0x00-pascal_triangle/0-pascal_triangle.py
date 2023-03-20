#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing the Pascal's triangle of a given integer.
    '''
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        a = []
        for j in range(i + 1):
            if j == 0 or j == i:
                a.append(1)
            elif i > 0 and j > 0:
                a.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(a)
    return triangle
