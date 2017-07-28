#!/usr/bin/python
# https://projecteuler.net/problem=2

from itertools import islice, takewhile
from library import fibonacci


if __name__ == '__main__':
    my_iterator = takewhile(lambda x: x < 4000000, fibonacci())
    # a quick pattern analysis indicates that every third Fibonacci number
    # is even, starting at 2.
    my_iterator = islice(my_iterator, 1, None, 3)
    total = sum(my_iterator)
    print('The answer is {}.'.format(total))

