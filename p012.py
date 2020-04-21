# Project Euler Problem 12 Solution
# 
# Author: Josh Douglas
#
# https://github.com/jsh-douglas/euler
# https://projecteuler.net/problem=12

from common.factors import factors

i = 1
iTriangle = 1
while True:
    if len(factors(iTriangle)) > 500:
        print(iTriangle)
        break
    else:
        i += 1
        iTriangle += i