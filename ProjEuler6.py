#!/usr/bin/python
# https://projecteuler.net/problem=6

def method1():
    '''Algebraically, the difference between the square of the sum and sum of squares is
       twice the sum of the pairwise produces between distinct summands.'''  
    total1 = 0

    for i in range(1,101):
        for j in range(i+1,101):
	    total1 += i*j
    total1 *= 2
    print "The answer via method 1 is: %d"%(total1,)

def method2():
    '''This is just the naive computation, not being clever.'''
    sqSum = sum(range(1,101))**2
    sumSq = sum(i**2 for i in range(1,101))
    total2 = sqSum - sumSq
    print "The answer via method 2 is: %d"%(total2,)

if __name__ == '__main__':
    import timeit
    print timeit.timeit("method1()", setup="from __main__ import method1",number=1)
    print timeit.timeit("method2()", setup="from __main__ import method2",number=1)

# it turns out method2 is faster by two orders of magnitude.
# Analysis of method1:
# two operations repeated 
