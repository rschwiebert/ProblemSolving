#!/usr/bin/python
# https://projecteuler.net/problem=7

# What is the 10 001st prime number?
# I would have liked to use a sieve, but it seems bad to have to specify
# how long the array containing the sieve is. In this method, no choice is made.

primes = [2,3,5]

def divisorCheck(primes, candidate):
    '''Return True if the candidate is prime, False otherwise'''
    limit = candidate**0.5
    for p in primes:
        if p > limit:
            break
        elif candidate % p == 0:
            return False
    return True

i=6
while len(primes) < 10001:
    if divisorCheck(primes,i):
        primes.append(i)
    i += 1

print "The answer is: %d"%primes[-1]
       
    

