#!/usr/bin/python2.7
# https://projecteuler.net/problem=14
# Longest Collatz cycle starting under 10**6


from library import collatz


cache = {1: 1}
maxn, maxcyc = (1, 1)


def compute_cycles(n):
    """Return cycle count, computing it recursively, if necessary."""
    if n not in cache:
        result = 1 + compute_cycles(collatz(n))
        cache[n] = result
    return cache[n]

if __name__ == '__main__':
    # Go through candidates making use of the cache.
    for i in range(2, 10**6):
        answer = compute_cycles(i)
        if answer > maxcyc:
            maxcyc = answer
            maxn = i

    print("The answer is: {}.".format(maxn))