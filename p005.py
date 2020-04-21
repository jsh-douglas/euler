# Project Euler Problem 5 Solution
# 
# Author: Josh Douglas
#
# https://github.com/jsh-douglas/euler
# https://projecteuler.net/problem=5

nums = [11, 13, 16, 17, 19]
found = False
i = 2520
while found == False:
    suitable = True
    for num in nums:
        if i % num != 0:
            suitable = False
            break
    if suitable:
        print(i)
        break
    else:
        i += 2520