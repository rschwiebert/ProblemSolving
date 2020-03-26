#!/usr/bin/python
__author__ = 'ryan'

# https://projecteuler.net/problem=78

# let p(n) be the number of ways n identical coins can be partitioned into (nonempty) piles
# find the least value of n for which p(n) is divisible by one million


def f(k):
    """
    The k'th pentagonal number
    :param k:
    :return:
    """
    return int(k * (3 * k - 1) / 2)


def g(k):
    """
    The k'th pentagonal number
    :param k:
    :return:
    """
    return int(k * (3 * k + 1) / 2)


MODULUS = 10**6


class Partitions(object):
    def __init__(self):
        self.cache = {}

    def part(self, n):
        if n in self.cache:
            return self.cache[n]
        elif n == 0:
            return 1
        elif n < 0:
            return 0
        else:
            tmp = 0
            for i in range(1, n+1):
                a = self.part(n - f(i))
                b = self.part(n - g(i))
                if a == b == 0:
                    break  # Without this short-circuit, it was taking forever
                tmp += (-1)**(i+1)*(a + b)
            tmp = tmp % MODULUS  # No sense in storing digits that don't matter
            self.cache[n] = tmp
            return tmp


if __name__ == '__main__':
    thing = Partitions()
    cur = 1
    result = thing.part(cur)
    while result % 1000000 != 0:
        cur += 1
        result = thing.part(cur)
    print('found it {}'.format(cur))
