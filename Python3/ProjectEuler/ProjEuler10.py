#!/usr/bin/python
# https://projecteuler.net/problem=10

# Find the sum of all the primes below two million.

from library import primes_less_than

if __name__ == '__main__':
    total = sum(primes_less_than(2 * 10**6))
    print('The answer is: {}'.format(total))
