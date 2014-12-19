#!/usr/bin/python
# https://projecteuler.net/problem=3

def findPrimeFactor(n):
    '''Find and return a prime factor for the natural number n'''
    i = 2
    maxFactor = 1

    while i <= (n**0.5) + 1:
        if n%i == 0:
            return i
        else:
            i += 1
    return n

input = 600851475143
while True:
    factor = findPrimeFactor(input)
    if input == factor:
        break
    else:
        input /= factor

print "The answer is: %d "%factor
