#!/usr/bin/env python3
"""function that calculates sigma notation i^2"""


def summation_i_squared(n):
    """calculates sigma notation i^2"""
    
    if isinstance(n, int) and n > 0:
        return int((n * (1 + n)) * (2 * n + 1) / 6)
    else:
        return None
