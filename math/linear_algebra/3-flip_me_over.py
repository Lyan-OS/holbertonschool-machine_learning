#!/usr/bin/env python3
"""function to transpose a matrix"""

def matrix_transpose(matrix):
    """Transpose a matrix"""

    new = []
    for i in range(len(matrix[0])):
        for row in matrix:
            new.append(row[i])
    return new
