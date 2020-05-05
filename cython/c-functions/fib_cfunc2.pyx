cdef int fib_c(int n):
    if n < 2:
        return n
    return fib_c(n-2) + fib_c(n-1)


cpdef int fibonacci(int n):
    return fib_c(n)
