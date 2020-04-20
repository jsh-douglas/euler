# Project Euler Problem 4 Solution
# 
# Author: Josh Douglas
#
# https://github.com/jsh-douglas/euler
# https://projecteuler.net/problem=4

from common.palindrome import isPalindrome

largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if isPalindrome(product):
            if product > largest:
                largest = product

print(largest)