#!/usr/bin/python2.7
# https://projecteuler.net/problem=12
# What is the value of the first triangle number to have over five hundred divisors?

# STILL DOESN'T WORK FAST ENOUGH


def count_divisors(n):
    ctr = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            ctr += 1
    return ctr + 1


def method1():
    i = 3
    c1 = count_divisors(i-1)
    c2 = count_divisors(i)
    check = c1*c2/2
    while check < 1000:
        i += 1
        c2 = c1
        c1 = count_divisors(i)
        check = c1*c2/2
        #print check

import timeit
if __name__ == "__main__":
    x = timeit.timeit('method1()', setup='from ProjEuler12 import method1', number=1)
    print x
    # method1()