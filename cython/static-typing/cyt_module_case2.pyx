"""
Static typing for a simple Cython module.
"""


def subtract(int x, int y):
    cdef int result = x - y
    return result
