# Project Euler Problem 25 Solution
# 
# Author: Josh Douglas
#
# https://github.com/jsh-douglas/euler
# https://projecteuler.net/problem=25

a, b = 0, 1
sequence = [a]
while len(str(sequence[-1])) != 1000:
    a, b = b, a + b
    sequence.append(a)

print(sequence.index(sequence[-1]))
