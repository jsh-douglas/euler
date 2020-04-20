def isPrime(num):
    import math
    if num < 2:
        return False
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def primeSieve(limit):
    nums = [True] * limit
    nums[0] = nums[1] = False
    primes = []
    
    for (num, isPrime) in enumerate(nums):
        if isPrime:
            primes.append(num)
            for num in range(num * 2, limit, num):
                nums[num] = False
    return primes

