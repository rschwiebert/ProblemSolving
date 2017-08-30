#!/usr/bin/python
__author__ = 'ryan'
# https://projecteuler.net/problem=89
# How many numbers below 50,000,000 are the sum of a prime square, a prime cube, and a prime fourth power?

from library import primes_less_than
from itertools import product

# largest prime with square less than 50 mil: 7069
# largest prime with cube less than 50 mil: 367
# largest prime with fourth power less than 50 mil: 83

if __name__ == '__main__':
    results = set()
    group_a = [x**2 for x in primes_less_than(7070)]
    group_b = [x**3 for x in primes_less_than(368)]
    group_c = [x**4 for x in primes_less_than(84)]
    for x in group_c:
        for y in group_b:
            if x + y >= 50*10**6:
                break
            for z in group_a:
                candidate = x + y + z
                if candidate >= 50*10**6:
                    break
                results.add(candidate)

    print('The answer is: {}'.format(len(results)))