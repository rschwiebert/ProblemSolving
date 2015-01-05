#!/usr/bin/python
# https://projecteuler.net/problem=4

# largest palindromic number that's a product of three digit numbers
# This is the naive approach 

isPal = lambda s: s == s[::-1]

maxNum = 1
for i in range(100, 1000):
    for j in range(i, 1000):
        s = str(i*j)
        if int(s) > maxNum and isPal(s):
            maxNum = int(s)

print "The answer is: %d " % maxNum