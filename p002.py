# Project Euler Problem 2 Solution
# 
# Author: Josh Douglas
#
# https://github.com/jsh-douglas/euler
# https://projecteuler.net/problem=2

from common.fib import fib

sequence = fib(4000000)

print(sum([num for num in sequence if num % 2 == 0 in sequence]))