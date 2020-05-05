"""
Static typing for a simple Cython module.
"""


def subtract(x, y):
    cdef int result = x - y
    return result
