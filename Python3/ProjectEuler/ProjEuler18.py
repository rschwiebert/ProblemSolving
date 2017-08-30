#!/usr/bin/python
# https://projecteuler.net/problem=18
# Maximum weight path "downward" through a triangular array.

# It's straightforward to see that a bottom-up iterative approach yields the max path weight.

# Here we recover the triangle from a datafile and make it into a triangular array of integers.
if __name__ == '__main__':
    filename = 'PE18data.txt'
    with open(filename, 'r') as f:
        triangle = f.readlines()
    triangle = list(map(str.strip, triangle))
    triangle = [list(map(int, row.split(' '))) for row in triangle]

    # Here is the actual bottom-up algorithm.
    for i in reversed(list(range(len(triangle) - 1))):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1],)

    print("The answer is %d." % triangle[0][0])
