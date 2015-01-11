#!/usr/bin/python
__author__ = 'ryan'
# https://projecteuler.net/problem=22

# This program lifts a bunch of names out of a textfile, numerizes their letters, ascertains
# Their alphabetical rank, then computes a score
# The program computes the sum of all scores


def evaluate(s):
    """We use ord as a shortcut to return a capital letter's numeric value in the alphabet."""
    return sum([ord(c)-64 for c in s])


def solve():
    with open('PE22data.txt', 'r') as f:
        names = f.read()
    names = names.split('","')
    names.sort()
    names = map(evaluate, names)  # numeric value of name
    answer = sum([(pair[0]+1)*pair[1] for pair in enumerate(names)])  # weights entries by (1-based) index and sums
    print "The answer is %d." % answer


if __name__ == "__main__":
    solve()