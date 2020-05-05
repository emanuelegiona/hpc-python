"""
Static typing for a simple Cython module.
"""


def subtract(float x, float y):
    cdef float result = x - y
    return result
