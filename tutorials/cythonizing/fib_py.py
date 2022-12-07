def fib_py(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = a + b, a
    return a