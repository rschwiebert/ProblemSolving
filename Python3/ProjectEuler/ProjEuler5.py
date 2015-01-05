#!/usr/bin/python
# https://projecteuler.net/problem=5

# Find the LCM of 1-20 

def euclidAlg(a,b):
    """Implement the Euclidean algorithm to find GCDs"""
    a,b = [max(a,b),min(a,b)]
    while a%b != 0:
        a, b = [b, a%b]
    return b

def myLCM(a,b):
    """Find the LCM via the formula LCM(x,y)=x*y/gcd(x,y)"""
    return a*b/euclidAlg(a,b)

answer = 2
for i in range(3,21):
    answer = myLCM(answer,i)

print("The answer is: %d "%answer)


