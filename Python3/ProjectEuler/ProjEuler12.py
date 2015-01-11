#!/usr/bin/python2.7
# https://projecteuler.net/problem=12
# What is the value of the first triangular number to have over five hundred divisors?

# Notes:
# We take advantage of the fact that a triangular number T factors as 2*T=n*(n+1)
# Since n and n+1 are coprime, we only need to find their factors (dividing one of them by 2)
# and because they are coprime, the number of divisors of their product is the product of their number
# of divisors.
# Since these two quantities are very close to the square root of T, we save a lot of time by not factoring T itself.

# Stategy:
# The strategy is to use a sieve to keep track of divisors. We do not have to complete the entire sieve: we can
# progressively check to see if we have an answer yet before continuing to build the sieve.


def solve():
    sieve = [1, 2]*6200
    sieve.insert(0, 0)
    for i in range(3, len(sieve)):
        j = 1
        while i*j < len(sieve):
            sieve[i*j] += 1
            j += 1
        if (i-1) % 2 == 0 and (sieve[(i-1)//2]*sieve[i]) > 500:
            y = i*(i+1)/2
            print("The answer is %d, which is %d in the triangular number sequence." % (y, i-1))
            return None
        elif (i-1) % 2 == 1 and (sieve[i-1]*sieve[i//2]) > 500:
            y = i*(i-1)/2
            print("The answer is %d, which is %d in the triangular number sequence." % (y, i-1))
            return None

if __name__ == "__main__":
    solve()
