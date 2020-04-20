# Project Euler Problem 9 Solution
# 
# Author: Josh Douglas
#
# https://github.com/jsh-douglas/euler
# https://projecteuler.net/problem=9

def pythagorianTriplet():
    c = 1
    while True:
        for b in range(1, c):
            for a in range(1, b):
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                        return a * b * c
        c += 1

print(pythagorianTriplet())