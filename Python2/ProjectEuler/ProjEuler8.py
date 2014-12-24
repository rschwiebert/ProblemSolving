#!/usr/bin/python
# https://projecteuler.net/problem=8

# Find the largest possible product of 13 consecutive digits in this number.

# Notes:

# This is an optimized version of the naive approach of just looking at 
# every window of 13 consecutive characters.
# I made it into an object that can take longer strings and window lengths.
# It's quite fast for the test case, often taking just under a millisecond.

text=('73167176531330624919225119674426574742355349194934'
'96983520312774506326239578318016984801869478851843'
'85861560789112949495459501737958331952853208805511'
'12540698747158523863050715693290963295227443043557'
'66896648950445244523161731856403098711121722383113'
'62229893423380308135336276614282806444486645238749'
'30358907296290491560440772390713810515859307960866'
'70172427121883998797908792274921901699720888093776'
'65727333001053367881220235421809751254540594752243'
'52584907711670556013604839586446706324415722155397'
'53697817977846174064955149290862569321978468622482'
'83972241375657056057490261407972968652414535100474'
'82166370484403199890008895243450658541227588666881'
'16427171479924442928230863465674813919123162824586'
'17866458359124566529476545682848912883142607690042'
'24219022671055626321111109370544217506941658960408'
'07198403850962455444362981230987879927244284909188'
'84580156166097919133875499200524063689912560717606'
'05886116467109405077541002256983155200055935729725'
'716362695618826704282524836008232575304207529634507316717')

class Solution:
    def __init__(self, string, length):
        self.s = string
        self.L = length

    def windowProd(self,index):
        '''Needed to compute the product of the next L numbers, when it is nonzero'''
        P = 1
        for j in range(index,index+self.L):
            P *= int(self.s[j])
        return P

    def maxProd(self):
        i = 0
        M = 0
        prod = 0
        MAX = 9**self.L
        while i + 13 < len(self.s):
            if '0' in self.s[i:i+self.L]:
                while '0' in self.s[i:i+self.L]: #this while loop advances through trivial cases when 0 kills everything
                    i += 1
            elif self.s[i-1] == '0':
                prod = self.windowProd(i)
                i += 1
            else:
                prod /= int(self.s[i-1])
                prod *= int(self.s[i+self.L-1])
                i += 1
            if prod > M: M = prod
            if prod == MAX: break   #if this is reached, there is no point in continuing
        print "The answer is: %d" % M

if __name__ == "__main__":
    sol = Solution(text,13)
    sol.maxProd()

