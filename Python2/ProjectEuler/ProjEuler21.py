#!/usr/bin/python
__author__ = 'ryan'
# https://projecteuler.net/problem=21

# This program locates "amicable" pairs of numbers below 10000 and then adds them

# Notes:
# This uses a sieve much like Project 12, except that instead of counting divisors, we're using it here to track the
# sum of proper divisors.


def solve():
    sieve = [1]*10**4
    sieve.insert(0, 0)
    answer = 0
    for i in range(2, len(sieve)):
        if sieve[i] < i and sieve[sieve[i]] == i:
            answer += i + sieve[i]
        j = 2
        while i*j < len(sieve):
            sieve[i*j] += i
            j += 1
    print "The answer is %d." % answer

if __name__ == "__main__":
    solve()