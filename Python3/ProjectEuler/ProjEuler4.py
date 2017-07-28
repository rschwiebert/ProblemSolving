#!/usr/bin/python
# https://projecteuler.net/problem=4

# largest palindromic number that's a product of three digit numbers
# This is the naive approach 

isPal = lambda s: s == s[::-1]


if __name__ == '__main__':
    maxNum = 1
    for i in range(100, 1000):  # do I really need to do all these?
        for j in range(i, 1000):
            k = i*j
            if k > maxNum and isPal(str(k)):  # is it more efficient to reverse?
                maxNum = k

    print("The answer is: {}".format(maxNum))
