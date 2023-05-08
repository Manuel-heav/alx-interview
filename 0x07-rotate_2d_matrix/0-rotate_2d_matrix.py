#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
		# Transpose the matrix
    for i in range(len(matrix)):
      for j in range(i, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

		# Reverse the amatrix
    N = len(matrix)
    for i in range((int)(N/2)):
      for j in range(N):
        matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]
