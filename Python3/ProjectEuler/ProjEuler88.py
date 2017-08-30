#!/usr/bin/python
__author__ = 'ryan'
# https://projecteuler.net/problem=88
# What is the sum of all the minimal product-sum numbers for 2<=k<=12000?

# method below is too slow. You basically need to check every partition of every factorization of every number
# until you hit the right answer.

from collections import deque, namedtuple
from copy import copy

Item = namedtuple('Item', ['sum', 'prod', 'list'])


def ndec_list_incrementer(ndec):
    """
    Walks a nondecreasing list, yielding nondecreasing lists which have sum
    one greater than the input list.
    :param ndec_list: a nondecreasing list of positive integers
    """
    fake_list = list(ndec.list) + [ndec.list[-1] + 1]
    i = 0
    while i < len(ndec.list):
        if fake_list[i] == fake_list[i + 1]:
            i += 1
            continue
        new_list = list(ndec.list)
        new_sum = ndec.sum + 1
        new_prod = ndec.prod / new_list[i] * (new_list[i] + 1)
        new_list[i] += 1
        new_list = tuple(new_list)
        new_item = Item(sum=new_sum, prod=new_prod, list=new_list)
        yield new_item
        i += 1


def ndec_list_generator(N):
    """
    Generates a sequence level-traversing a tree of nondecreasing sequences
    :param N: the length of the list of integers 
    """
    Q = deque()
    seen = set()
    first = Item(sum=N, prod=1, list=(1,) * N)
    Q.appendleft(first)
    while Q:
        cur = Q.pop()
        yield cur
        if cur not in seen:
            seen.add(cur)
            Q.extendleft(ndec_list_incrementer(cur))

if __name__ == '__main__':
    results = set()
    for i in range(2, 12001):
        ndec_iter = ndec_list_generator(i)
        for item in ndec_iter:
            if item.sum != item.prod:
                continue
            else:
                break
        print('Found {} for {}.'.format(item, i))
        results.add(item.sum)
    print("The answer is: {}".format(sum(results)))
