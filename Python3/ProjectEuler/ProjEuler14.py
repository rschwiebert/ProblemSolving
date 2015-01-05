#!/usr/bin/python2.7
# https://projecteuler.net/problem=14
# Longest Collatz cycle starting under 10**6


def collatz(n):
    """Implementation of Collatz function."""
    if n % 2 == 0:
        out = n/2
    else:
        out = 3*n+1
    return out

cache = {1: 1}
maxn, maxcyc = (1, 1)


def compute_cycles(n):
    """Return cycle count, computing it recursively, if necessary."""
    if n not in cache:
        result = 1 + compute_cycles(collatz(n))
        cache[n] = result
    return cache[n]


# Go through candidates making use of the cache.
for i in range(2, 10**6):
    answer = compute_cycles(i)
    if answer > maxcyc:
        maxcyc = answer
        maxn = i

print("The answer is %d." % maxn)