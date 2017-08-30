#!/usr/bin/python2.7
# https://projecteuler.net/problem=16
# Sum of digits of 2**1000


if __name__ == '__main__':
    answer = sum(int(digit) for digit in str(2**1000))

    print("The answer is %d." % answer)
