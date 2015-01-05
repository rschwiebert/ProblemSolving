#!/usr/bin/python
__author__ = 'ryan'
# https://projecteuler.net/problem=67
# Maximum weight path "downward" through a triangular array.

# It's straightforward to see that a bottom-up iterative approach yields the max path weight.
# This is EXACTLY the same solution used in Project 18.
# The complexity is linear in the number of rows in the triangle.


# Here we recover the triangle from a datafile and make it into a triangular array of integers.
filename = 'PE67data.txt'
with open(filename, 'r') as f:
    triangle = f.readlines()
triangle = map(str.strip, triangle)
triangle = [map(int, row.split(' ')) for row in triangle]

# Here is the actual bottom-up algorithm.
for i in reversed(range(len(triangle) - 1)):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1],)

print "The answer is %d." % triangle[0][0]