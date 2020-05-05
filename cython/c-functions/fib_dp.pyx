cpdef int fibonacci(int n):
    if n < 2:
        return n

    cdef list array = [1 if a == 1 else 0 for a in range(n+1)]
    if array[n-1] == 0:
        array[n-1] = fibonacci(n-1)

    if array[n-2] == 0:
        array[n-2] = fibonacci(n-2)

    array[n] = array[n-2] + array[n-1]
    return array[n]
