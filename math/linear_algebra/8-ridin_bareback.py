#!/usr/bin/env python3
"""Function that multiplies two matrices"""


def mat_mul(mat1, mat2):
    """Performs matrix multiplication on two 2D matrices."""
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(a * b for a, b in zip(row, col))
             for col in zip(*mat2)] for row in mat1]
