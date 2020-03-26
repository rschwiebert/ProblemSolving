#!/usr/bin/python2.7
# https://projecteuler.net/problem=9


# There exists one pythagorean triple (a,b,c) such that a+b+c=1000. Find the product a*b*c

# Notes:
# Method 2 is more sophisticated than method 1, and performs 10,000 times faster.
# Method1 has three nested loops, probably putting it into O(n^3) performance
# Method2 is just searching a finite ternary tree, so it would have O(n) performance

from collections import deque
from library import FibBox


# Naive (slow) method
def method1():
    a, b, c = (0, 0, 0)
    squares = [i ** 2 for i in range(0, 1001)]  # c is in this range, so this covers all possible c^2
    for a in range(1, 1001):
        for b in range(a, 1001):
            if a ** 2 + b ** 2 in squares:
                c = (a ** 2 + b ** 2) ** 0.5
                c = int(c)
                if a + b + c == 1000:
                    print("The triple is:", a, b, c)
                    print("The answer is abc= ", a * b * c)
                    break
                else:
                    continue


# Fibonacci box method (much faster)
def method2():
    """Using Fibonacci boxes to generate primitive and nonprimitive
       Pythagorean triples, do a DFS of the tree to find our answer"""
    stack = deque([FibBox((1, 1, 2, 3))])
    while stack:
        cur = stack.pop()
        if cur.total <= 1000:
            if 1000 % cur.total == 0:  # here is the check to see if the triple has been found
                factor = 1000 / cur.total
                print('The answer is: {}'.format(cur.product * factor ** 3))
                return
            else:  # continuing the traversal of the primitive tree
                cur.set_children()
                stack.extend(cur.children)


if __name__ == "__main__":
    method2()
