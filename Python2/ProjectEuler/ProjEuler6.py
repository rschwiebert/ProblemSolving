#!/usr/bin/python
# https://projecteuler.net/problem=6

# Notes:
# This is just the naive computation, not being clever.'''

sqSum = sum(range(1,101))**2
sumSq = sum(i**2 for i in range(1,101))
total2 = sqSum - sumSq
print "The answer via method 2 is: %d"%(total2,)


