def isPrime(num):
    import math
    if num < 2:
        return False
    for i in range(2, math.ceil(math.sqrt(num))):
        if num % i == 0:
            return False
    return True
