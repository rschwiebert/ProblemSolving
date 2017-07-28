#!/usr/bin/python
# https://projecteuler.net/problem=1


from library import gauss_sum

if __name__ == '__main__':
    total = 3 * gauss_sum(1000 // 3)
    total += 5 * gauss_sum((1000 // 5) - 1)  # otherwise we accidentally pick up 5000
    total -= 15 * gauss_sum(1000 // 15)  # we double-counted these
    print('The answer is {}.'.format(total))
