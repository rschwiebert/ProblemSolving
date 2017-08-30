#!/usr/bin/python2.7
# https://projecteuler.net/problem=15
__author__ = 'ryan'

# How many paths are there through a 20x20 grid from top left to bottom right if you can move "right" or "down"
# at each step?

# Same thing as counting binary sequences with 20 0's and 20 1's.

from itertools import product


def solve(n):
    n = n + 1
    grid = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        # The top and left edges can only be accessed by a single path
        grid[0][i] = 1
        grid[i][0] = 1
    for (a, b) in product(list(range(1, n)), list(range(1, n))):
        # every other intersection can only be accessed by the intersection above or to the left of it
        grid[a][b] = grid[a-1][b] + grid[a][b-1]
    print("The answer is %d." % grid[n-1][n-1])

if __name__ == "__main__":
    solve(20)