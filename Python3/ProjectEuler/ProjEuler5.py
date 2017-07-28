#!/usr/bin/python
# https://projecteuler.net/problem=5

# Find the LCM of 1-20 

from library import lcm


if __name__ == '__main__':
    answer = 2
    for i in range(3, 21):
        answer = lcm(answer, i)

    print("The answer is: {}".format(answer))


