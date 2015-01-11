#!/usr/bin/python
__author__ = 'ryan'
# https://projecteuler.net/problem=22

# This program lifts a bunch of names out of a textfile, numerizes their letters, ascertains
# Their alphabetical rank, then computes a score
# The program computes the sum of all scores


def evaluate(s):
    """Use ord() to recover letter values."""
    return sum(ord(c)-64 for c in s)


def solve():
    with open('PE22data.txt', 'r') as f:
        names = f.read()
    names = names.split('","')
    names.sort()
    names = list(map(evaluate, names))
    answer = sum((pair[0]+1)*pair[1] for pair in enumerate(names))  # weights each by (1-based) index and sums
    print("The answer is %d." % answer)


if __name__ == "__main__":
    solve()
