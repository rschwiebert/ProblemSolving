#!/usr/bin/python
# https://projecteuler.net/problem=1

total = 0
for i in range(1000):
    if i%3 == 0:
        total += i
    elif i%5 == 0:
        total += i
    else:
        pass

print "The answer is: %d "%total
