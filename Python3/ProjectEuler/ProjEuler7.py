#!/usr/bin/python
# https://projecteuler.net/problem=7

# What is the 10 001st prime number?

from library import primes_less_than
from itertools import islice

if __name__ == '__main__':
    p = None
    for p in islice(primes_less_than(10**6), 0, 10001):
        pass
    print('The answer is: {}'.format(p))
