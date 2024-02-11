#!/usr/bin/python3
"""

The lazy_matrix_mul module.

"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ calculates the matrix multiplication of two matrices"""
    return numpy.matmul(m_a, m_b)
