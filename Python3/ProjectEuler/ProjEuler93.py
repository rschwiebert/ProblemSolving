#!/usr/bin/python
__author__ = 'ryan'

# https://projecteuler.net/problem=93

# Find a set of four distinct digits which can be used with four operations +-*/ to
# make the largest list of consecutive positive integers 1..n possible
# Give the answer as abcd with a<b<c<d

# Create a "syntax tree" with a branching factor of four and depth 3, and pipe combinations of four digits in.
# Then, sort the leaves and search for the longest run starting at zero

from itertools import combinations
from fractions import Fraction
from collections import deque, defaultdict
from copy import copy
from bisect import insort

from time import time

digits = tuple([Fraction(x) for x in range(10)])


def create_holder():
    """Utility to populate the results defaultdict"""
    v = bytearray(b'\x00'*5000)
    v[0] = 1
    return v


if __name__ == '__main__':
    t0 = time()
    d2 = deque([])
    d3 = deque([])
    for a, b in combinations(digits, 2):
        d2.append([a+b, [a.numerator, b.numerator]])
        d2.append([a*b, [a.numerator, b.numerator]])
        d2.append([a-b, [a.numerator, b.numerator]])
        d2.append([b-a, [a.numerator, b.numerator]])
        if b != 0:
            d2.append([a/b, [a, b]])
        if a != 0:
            d2.append([b/a, [a, b]])
    t1 = time()
    print(t1 - t0)
    for c in digits:
        for X, lst in d2:
            if c not in lst:
                new_list = copy(lst)
                insort(new_list, c.numerator)

                d3.append([c+X, new_list])
                d3.append([c*X, new_list])
                d3.append([c-X, new_list])
                d3.append([X-c, new_list])
                if c != 0:
                    d3.append([X/c, new_list])
                if X != 0:
                    d3.append([c/X, new_list])
    t2 = time()
    print(t2-t1)

    results = defaultdict(create_holder)
    for c in digits:
        for X, lst in d3:
            if c not in lst:
                new_list = copy(lst)
                insort(new_list, c.numerator)
                key = tuple(new_list)
                values = list()
                values.append(c+X)
                values.append(c*X)
                if c > X:
                    values.append(c-X)
                else:
                    values.append(X-c)
                if X != 0:
                    values.append(c/X)
                if c != 0:
                    values.append(X/c)
                for result in values:
                    if result.denominator == 1 and result.numerator >= 0:
                        results[key][result.numerator] = 1
    t3 = time()
    print(t3-t2)

    record = 1
    record_holder = None
    for key, data in results.items():
        cur = record
        ok = True
        while cur > 1:
            if data[cur] == 0:
                ok = False
                break
            cur -= 1

        if ok is True:
            while True:
                if data[record + 1] == 1:
                    record += 1
                    continue
                else:
                    record_holder = key
                    # print('new streak: {} Record holder: {}'.format(key, record))
                    break
    t4 = time()
    print(t4-t3)
    print('total elapsed {}'.format(t4-t0))
    print("record holder: {}".format(record_holder))
