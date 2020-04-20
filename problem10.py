# Project Euler Problem 10 Solution
# 
# Author: Josh Douglas
#
# https://github.com/jsh-douglas/euler
# https://projecteuler.net/problem=10

from common.prime import primeSieve

print(sum(primeSieve(2_000_000)))
