#!/usr/bin/env python3
"""function that concatenates two arrays"""


def cat_arrays(arr1, arr2):
    """concatenates two arrays"""
    new = []
    j = 0
    for i in range(len(arr1) + len(arr2)):
        if i < len(arr1):
            new.append(arr1[i])
        else:
            new.append(arr2[j])
            j += 1
    return new
