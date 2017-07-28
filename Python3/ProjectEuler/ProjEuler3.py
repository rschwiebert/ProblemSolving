#!/usr/bin/python
# https://projecteuler.net/problem=3

from array import array


from library import primes_less_than


def findPrimeFactor(n):
    """Find and return the lowest prime factor of n"""
    i = 2

    while i <= (n**0.5) + 1:
        if n % i == 0:
            return i
        else:
            i += 1
    return n


def method1():
    number = 600851475143

    # The answer will be the last prime factor found in this sequence
    while True:
        factor = findPrimeFactor(number)
        if number == factor:
            break
        else:
            number /= factor

    print("The answer is: %d " % factor)


def method2():
    number = 600851475143
    largest_factor = 0
    for p in primes_less_than(775147):  # 775147 is rounded sqrt of `number`
        if number == 1:
            break
        if number % p == 0:
            largest_factor = p
            while number % p == 0:
                number /= p
    print("The answer is: {}".format(largest_factor))

if __name__ == "__main__":
    method2()
