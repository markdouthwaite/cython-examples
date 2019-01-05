
def fibonacci(n):
    """
    Print the Fibonacci series up to n.
    """
    
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b


cpdef int fibonacci_faster(int n):
    """
    Print the Fibonacci series up to n.
    """
    cdef int a = 0
    cdef int b = 1
    while b < n:
        a = b
        b = a + b
    return b