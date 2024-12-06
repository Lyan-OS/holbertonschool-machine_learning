#!/usr/bin/env python3
"""function to transpose a matrix"""

def matrix_transpose(matrix):
    """Transpose a matrix"""

    full = []
    for i in range(len(matrix[0])):
        new = []
        for j in range(len(matrix)):
            new.append(matrix[j][i])
        full.append(new)
    return full
