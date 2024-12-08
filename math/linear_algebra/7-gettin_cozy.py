#!/usr/bin/env python3
"""concatenates two 2D matrices along a specific axis"""


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along a specified axis."""
    if not mat1 and not mat2:
        return []
    if not mat1 or not mat2:
        return None

    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row.copy() for row in mat1] + [row.copy() for row in mat2]

    if axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
