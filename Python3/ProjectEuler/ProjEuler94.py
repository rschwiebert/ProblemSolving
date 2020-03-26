#!/usr/bin/python
__author__ = 'ryan'

# https://projecteuler.net/problem=94

# An almost equilateral triangle is one in which two sides are equal and
# the third side differs by the equal sides by exactly 1
# Find the sum of perimeters of almost equilateral triangles with integer area,
# whose perimeters do not exceed 10**9

# Each parameter L > 1 defines two almost equilateral triangles.
# By Heron's formula, the area is (1/4)sqrt(3L^2+2L-1) or (1/4)sqrt(3L^2-2L-1), depending on the off-by-one side
# We can first check to see if the quantity under the sqrt is divisible by 16, then proceed to check if it is a
# perfect square.
# We can stop checking when 3L - 1 > 10**9
# The numbers are small enough that int(sqrt(L))**2 == L should be able to reliably detect squareness, I think

from math import sqrt
from itertools import cycle
from time import time


def naive_is_square(n):
    s = int(sqrt(n))
    if n == s ** 2:
        return s


def is_square(n):
    s = str(n).zfill(4)
    a, b, c, d = map(int, s[-4:])

    mod_10 = d
    if mod_10 not in {0, 1, 4, 5, 6, 9}:
        return False
    if mod_10 == 6 and c % 2 == 0:
        return False
    if mod_10 == 5 and c != 2:
        return False
    if mod_10 in {0, 1, 4, 9} and c % 2 == 1:
        return False
    if mod_10 in {1, 9} and 10 * b + c % 4 != 0:
        return False

    if n % 7 not in {0, 1, 2, 4}:
        return False

    if n % 8 not in {0, 1, 4}:
        return False

    if n % 9 not in {0, 1, 4, 7}:
        return False

    if n % 13 not in {0, 1, 3, 4, 9, 10, 12}:
        return False


if __name__ == '__main__':
    t0 = time()
    limit = (10 ** 9 + 2) // 3
    L = 1
    # Experimentally, L must be 1, 5 or 7 mod 10?
    total = 0
    # for inc in cycle([4, 6]):
    for inc in cycle([4, 2, 4, ]):
        L += inc
        if 3*L - 1 > 10**9:
            break

        Q1 = 3 * L ** 2 + 2 * L - 1
        if Q1 % 16 == 0:
            Q1 = Q1 // 16
        sq = naive_is_square(Q1)
        if sq:
            print('found one: {} {} {} {} ({}, {})'.format(L, L, L - 1, 3*L+1, Q1, sq * L))
            total += 3 * L - 1

        Q2 = 3 * L ** 2 - 2 * L - 1
        if Q2 % 16 == 0:
            Q2 = Q2 // 16
        sq = naive_is_square(Q2)
        if sq:
            print('found one: {} {} {} {} ({}, {})'.format(L, L, L + 1, 3*L-1, Q2, sq * L))

            total += 3 * L + 1

    print(total)
    print(time()-t0)