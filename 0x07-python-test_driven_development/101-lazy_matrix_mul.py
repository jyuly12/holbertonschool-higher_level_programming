#!/usr/bin/python3
"""
This module multiplies 2 matrices by using the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    Returns the result of the multiplication of two matrices
    """
    return numpy.matmul(m_a, m_b)
