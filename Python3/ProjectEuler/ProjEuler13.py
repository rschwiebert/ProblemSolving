#!/usr/bin/python2.7
# https://projecteuler.net/problem=13
# The first ten (on the left) digits of a large sum of large numbers.


# The grade school addition algorithm seems necessary and efficient.
# Potentially all of the digits of the number could influence the top 10,
# so the sum really needs to be computed.


answerdigits = []
with open('PE13data.txt', 'r') as f:
    numbers = f.readlines()

numbers = list(map(str.strip, numbers))

carry = 0
i = 1
while i <= 50:
    temp = sum([int(x[-i]) for x in numbers])
    carry += temp
    answerdigits.insert(0, carry % 10)
    carry = carry//10
    i += 1

carry = str(carry)
carry = list(map(int, carry))
answerdigits = carry + answerdigits[:10]

answer = answerdigits[:10]
answer = list(map(str, answer))
answer = ''.join(answer)

print("The answer is %s" % answer)