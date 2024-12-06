#!/usr/bin/env python3
"""function that adds two matrices element-wise"""


def add_matrices2D(mat1, mat2):
    """adds two matrices element wise
    Returns: new list"""

    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    
    if not mat1 or not mat2:
        return None

    full = []
    for i in range(len(mat1[0])):
        new = []
        for j in range(len(mat1)):
            new.append(mat1[i][j] + mat2[i][j])
        full.append(new)
    return full


def matrix_shape(matrix):
    """Calculates the shape of a matrix."""
    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
