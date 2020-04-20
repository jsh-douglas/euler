# Project Euler Problem 3 Solution
# 
# Author: Josh Douglas
#
# https://github.com/jsh-douglas/euler
# https://projecteuler.net/problem=3

from common.factors import factors
from common.prime import isPrime

primeFactors = [num for num in factors(600851475143) if isPrime(num)]
print(primeFactors[-1])