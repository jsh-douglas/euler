def factors(num):
    import math
    factors = []
    for i in range(1, math.ceil(math.sqrt(num))):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return sorted(factors)
