#!/usr/bin/python
# https://projecteuler.net/problem=3


def findPrimeFactor(n):
    """Find and return the lowest prime factor of n"""
    i = 2

    while i <= (n**0.5) + 1:
        if n % i == 0:
            return i
        else:
            i += 1
    return n

number = 600851475143

# The answer will be the last prime factor found in this sequence
while True:
    factor = findPrimeFactor(number)
    if number == factor:
        break
    else:
        number /= factor

print("The answer is: %d " % factor)
