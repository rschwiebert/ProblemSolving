#!/usr/bin/python
__author__ = 'ryan'
# https://projecteuler.net/problem=20
# Sum of digits of a large factorial

# Python "just works" on large integers, so this solution is possible.

product = 1

for i in range(1, 101):
    product *= i
    if i % 10 == 0 and i > 0:
        product //= 100   # every 10 factors, we encounter 2, 5 and 10. They don't contribute digits.

answer = sum(int(digit) for digit in str(product))

print("The answer is %d." % answer)
