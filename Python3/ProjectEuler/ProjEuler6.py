#!/usr/bin/python
# https://projecteuler.net/problem=6

# Notes:
# This is just the naive computation, not being clever.'''

from library import gauss_sum, sum_of_squares


def method_2():
    sqSum = sum(range(1, 101))**2
    sumSq = sum(i**2 for i in range(1, 101))
    total2 = sqSum - sumSq
    print("The answer via method 2 is: %d" % (total2,))


if __name__ == '__main__':
    N = 100
    sosq = sum_of_squares(N)
    sqos = gauss_sum(N) ** 2
    answer = sqos - sosq
    print('The answer is: {}'.format(answer))
