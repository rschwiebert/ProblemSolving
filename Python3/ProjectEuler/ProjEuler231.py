#!/usr/bin/python
# https://projecteuler.net/problem=231

# Find the sum of the terms in the prime factorisation of Binom(2*10**7,15*10**6)

# Notes:
# We basically need to track prime factorizations between 5*10**6+1 and 2*10**7

from collections import defaultdict

primes = [2,3,5,7,11]
factorizations = defaultdict(list)
answer = defaultdict(int)

def genPrimes():
    '''Store primes up to 15*10**6 for use later.
       This makes sense because we will need them all.'''
    i = 13
    while primes[-1]<2*10**7:
        isPrime = True
        for p in primes:
            if p > i**0.5:
                break
            elif i % p == 0:
                isPrime = False
                break
            else:
                continue
        if isPrime: 
            primes.append(i)
        i += 2

def findFactor(n):
    '''This finds a prime factor and returns it.'''
    for p in primes:
        if p > n**0.5:
            return n
        elif i % p == 0:
            return p
        else:
            continue

def factorize(n):
    '''Uses a cache to factorize n, and returns an unordered list of prime factors'''
    if n in factorizations:
        return factorizations[n]
    else:
        p = findFactor(n)
        factors = [p]
        factors.extend(factorize(n/p))
        factorizations[n] = factors
        return factors

# Now we drive the factorize function through the relevant range,
# keeping a tally of the prime factors that occur
    
for i in range(2*10**7+1):
    factors = factorize(i)
    for p in factors:
        answer[p] += 1

total = 0
for p in answer:
    total += p*answer[p]

print "The answer is: %d"%total




