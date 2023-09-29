#!/usr/bin/python3

""" Two matrices"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Two matrices.
    Args:
         The first matrix.
         The second matrix.
    """

    return (np.matmul(m_a, m_b))
