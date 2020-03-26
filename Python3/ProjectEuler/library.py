from array import array
from collections import deque


def fibonacci():
    """
    A generator for Fibonacci numbers. The sequence starts 1, 2, 3, 5,... 
    """
    i, j = 1, 1
    while True:
        yield j
        i, j = j, i + j


def triangular():
    """
    A generator for triangular numbers. The sequence starts 1, 3, 6,...
    """
    i = 0
    n = 1
    while True:
        i += n
        yield i
        n += 1


def collatz(n):
    """Implementation of Collatz function."""
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def euclid_alg(a, b):
    """Implement the Euclidean algorithm to find GCDs"""
    a, b = [max(a, b), min(a, b)]
    while a % b != 0:
        a, b = [b, a % b]
    return b


def lcm(a, b):
    """Find the LCM via the formula LCM(x,y)=x*y/gcd(x,y)"""
    return a * b / euclid_alg(a, b)


def gauss_sum(n):
    """
    Return the sum of integers 1...n
    :param n: input integer
    :return: sum of integers 1...n using Gauss's trick
    """
    return n * (n + 1) / 2


def sum_of_squares(n):
    """
    Return the sum of squares of integers 1...n
    :param n: input integer
    :return: sum of squares of integers 1...n using the formula
    """
    return n * (n + 1) * (2 * n + 1) / 6.0


def primes_less_than(N):
    """
    :param N: length of the sieve 
    :return: yield the next prime that we find
    """
    sieve = array('b', [0] * N)
    for i in range(2, N):
        if sieve[i] != 0:
            continue
        yield i
        for j in range(2 * i, N, i):
            sieve[j] = 1


class FibBox:
    """
    Basic implementation of a Fibonacci box tree node.
    This is useful for generating primitive pythagorean triples
    """

    def __init__(self, v):
        (self.a, self.b, self.c, self.d) = v
        self.triple = (
            self.b * self.d,
            2 * self.a * self.c,
            self.a * self.d + self.b * self.c
        )
        self.total = sum(self.triple)
        self.product = self.triple[0] * self.triple[1] * self.triple[2]
        self.children = []

    def set_children(self):
        self.children = (
            FibBox((self.d - self.b, self.b, self.d, 2 * self.d - self.b)),
            FibBox((self.b, self.d, self.b + self.d, 2 * self.b + self.d)),
            FibBox((self.d, self.b, self.b + self.d, 2 * self.d + self.b)),
        )


def pythag_triple_gen(limiting_function=None, max_=None):
    """
    Produce primitive pythagorean triples
    :param limiting_function: function to apply to self.triple to compare with max
    :param max: If an integer, limit the max of triples returned with this number.
                If None, produce all triples.
    """
    stack = deque([FibBox((1, 1, 2, 3))])
    while stack:
        cur = stack.pop()
        yield cur.triple
        cur.set_children()
        if limiting_function is not None:
            stack.extend([ch for ch in cur.children if limiting_function(ch.triple) <= max_])
        else:
            stack.extend(cur.children)
