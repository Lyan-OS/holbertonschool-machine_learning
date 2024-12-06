#!/usr/bin/env python3
"""Function that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """adds two arrays element-wise"""
    if matrix_shape(arr1) != matrix_shape(arr2):
        return None
    new = []
    for i in range(len(arr1)):
        new.append(arr1[i] + arr2[i])
    return new

def matrix_shape(matrix):
    """Calculates the shape of a matrix."""
    shape = []

    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape