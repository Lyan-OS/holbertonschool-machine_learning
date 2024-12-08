#!/usr/bin/env python3
"""function that performs element wise add, sub, mul and div"""
import numpy as np


def np_elementwise(mat1, mat2):
    """Performs element-wise add, sub, mul, and div."""
    return mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2
