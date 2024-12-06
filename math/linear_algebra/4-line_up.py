#!/usr/bin/env python3
"""Function that adds two arrays element-wise"""


def add_arrays(arr1, arr2):
    """adds two arrays element-wise

    Returns: new list"""
    if len(arr1) != len(arr2):
        return None

    new = []
    for i in range(len(arr1)):
        new.append(arr1[i] + arr2[i])
    return new
