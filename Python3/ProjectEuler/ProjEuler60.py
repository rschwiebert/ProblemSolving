#!/usr/bin/python
__author__ = 'ryan'
# https://projecteuler.net/problem=60

# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

# Notes:
# The goal is to find a 5-clique in a graph whose nodes are prime numbers
# The only obvious extra structure I can see to the problem is that the
# winning candidate must consist of a subset of the numbers which are 1 mod 3 and maybe 3
# or a subset of the numbers which are 2 mod 3 and maybe 3. The 1 mod 3 and 2 mod 3 sets
# cannot mix since that would create a number divisible by 3. This is also "halves" the size of the
# set you need to check to see if a concatenation is prime: two 1 mod 3's must be in the 2 mod 3 set, etc.
# Needless to say, 2 and 5 are right out.

from collections import defaultdict
from math import log
from library import primes_less_than
from itertools import combinations
from queue import deque

group_a = set([3])
group_b = set([3])
groups = {1: group_a, 2: group_b}
for p in primes_less_than(10 ** 8):
    if p in (2, 3, 5):
        continue
    if p % 3 == 1:
        group_a.add(p)
    if p % 3 == 2:
        group_b.add(p)


def concat(x, y):
    return x * 10**(int(log(y, 10)) + 1) + y


def is_adjacent(x, y):
    if x == 3:
        check = groups[y % 3]
    elif x % 3 == 1:
        check = groups[2]
    else:
        check = groups[1]
    return concat(x, y) in check and concat(y, x) in check


if __name__ == '__main__':
    print('starting')
    adjacency = defaultdict(set)
    for p, q in combinations(primes_less_than(10000), 2):
        if is_adjacent(p, q):
            adjacency[p].add(q)
    print('finished adjacency')
    Q = deque([[p] for p in primes_less_than(10000)])
    results = list()
    while Q:
        cur = Q.pop()
        test = True
        for q in cur[:-1]:
            if cur[-1] not in adjacency[q]:
                test = False
                break
        if test is True:
            if len(cur) == 5:
                results.append(cur)
                break
            for x in adjacency[cur[-1]]:
                toAdd = cur + [x]
                Q.appendleft(toAdd)

    print('The answer is: {}'.format(min(map(sum, results))))
