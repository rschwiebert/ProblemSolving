#!/usr/bin/python
# https://projecteuler.net/problem=2

v = [1,2]
total = 0

while v[1] < 4*(10**6):
    if v[1]%2 == 0:
        total += v[1]
    v = [v[1],v[0]+v[1]]

print("The answer is: %d "%total)
