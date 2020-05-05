cpdef int fibonacci(int n):
    if n < 2:
        return n

    cdef int a = 0
    cdef int b = 1
    cdef int c
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c

    return b
