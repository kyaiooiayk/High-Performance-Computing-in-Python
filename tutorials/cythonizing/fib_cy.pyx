def fib_cy(int n):
    cdef int a = 0
    cdef int b = 1
    cdef int i
    for i in range(n - 1):
        a, b = a + b, a
    return a