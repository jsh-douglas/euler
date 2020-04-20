# Project Euler Problem 7 Solution
# 
# Author: Josh Douglas
#
# https://github.com/jsh-douglas/euler
# https://projecteuler.net/problem=7

from common.prime import isPrime

primes = []
i = 1
while len(primes) < 10_001:
    if isPrime(i):
        primes.append(i)
    i += 1
    
print(primes[-1])