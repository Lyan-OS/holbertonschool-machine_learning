#!/usr/bin/env python3
"""function that concatenates two numpy.ndarrays along the specified axis"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenates two numpy.ndarrays along the specified axis."""
    return np.concatenate((mat1, mat2), axis=axis)
