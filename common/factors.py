def factors(num):
    import math
    factors = []
    for i in range(1, math.ceil(math.sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return sorted(list(set(factors)))
