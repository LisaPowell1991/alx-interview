#!/usr/bin/python3

""" A module containing rotate_2d_matrix function """


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degress clockwise in-place.

    Args:
    matrix (list of list  of int): A 2D list representing,
    the square matrix to be rotated.

    Return:
    Does not return anything, the matrix is modified in-place.
    """
    n = len(matrix)

    # Transpose matrix
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements at position(i, j) with elements at position(j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse rows
    for i in range(n):
        matrix[i].reverse()
