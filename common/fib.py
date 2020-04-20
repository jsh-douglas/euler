def fib(lim):
    a, b = 0, 1
    sequence = []
    while a < lim:
        sequence.append(a)
        a, b = b, a + b
    return sequence
