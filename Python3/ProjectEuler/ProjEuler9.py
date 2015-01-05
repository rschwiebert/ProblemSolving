#!/usr/bin/python2.7
# https://projecteuler.net/problem=9


# There exists one pythagorean triple (a,b,c) such that a+b+c=1000. Find the product a*b*c

# Notes:
# Method 2 is more sophisticated than method 1, and performs 10,000 times faster.
# Method1 has three nested loops, probably putting it into O(n^3) performance
# Method2 is just searching a finite ternary tree, so it would have O(n) performance

# Naive (slow) method
def method1():
    a,b,c=(0,0,0)
    squares=[i**2 for i in range(0,1001)] #c is in this range, so this covers all possible c^2
    for a in range(1,1001):
        for b in range(a,1001):
            if a**2+b**2 in squares:
                c=(a**2+b**2)**0.5
                c=int(c)
                if  a+b+c==1000:
                    print("The triple is:", a,b,c)
                    print("The answer is abc= ",a*b*c)
                    break
                else:
                    continue

class FibBox:
    '''Basic implementation of a Fibonacci box tree node'''
    def __init__(self, v):
        self.a = v[0]
        self.b = v[1]
        self.c = v[2]
        self.d = v[3]
        self.values=[self.a,self.b,self.c,self.d]
        self.triple = ( 2*self.a*self.c,
                        self.b*self.d,
                        self.a*self.d+self.b*self.c)
        self.children = []

    def setChildren(self):
        self.children = [FibBox((self.d-self.b,  self.b, self.d, 2*self.d-self.b)),
                FibBox((self.b, self.d, self.b+self.d, 2*self.b+self.d)),
                FibBox((self.d, self.b, self.b+self.d, 2*self.d+self.b)),
            ]
        
def checkMultiples(v):
    '''Generates all nonprimitive triples from a primitive one,
        and returns the winner, if it exists.'''
    i = 1
    temp = v
    while sum(temp) < 1000:
        temp = tuple([x*i for x in v])
        i += 1
    if sum(temp) == 1000:
        return temp
    else:
        return []

# Fibonacci box method (much faster)
def method2():
    '''Using Fibonacci boxes to generate primitive and nonprimitive
       Pythagorean triples, do a DFS of the tree to find our answer'''
    stack = [FibBox((1,1,2,3))]
    while stack != []:
        cur = stack.pop(-1)
        if sum(cur.triple) <= 1000:
            temp = checkMultiples(cur.triple)
            if temp:    #here is the check to see if the triple has been found
                break
            else:       #continuing the traversal of the primitive tree
                cur.setChildren()
                stack.extend(cur.children)
    if sum(temp) == 1000:
        print("The triple is: ", temp)
        print("The answer is abc=",temp[0]*temp[1]*temp[2])
    else:
        print("The triple wasn't found.")


if __name__ == "__main__":
    method2()
