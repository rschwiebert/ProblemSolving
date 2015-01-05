#!/usr/bin/python2.7
# https://projecteuler.net/problem=17
# Count characters used to spell out numbers 1-1000

ones = dict(list(zip([1, 2, 3, 4, 5, 6, 7, 8, 9],
            "one two three four five six seven eight nine".split(' '))))
ones[0] = ""
teens = dict(list(zip([10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
             "ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split(' '))))
tens = dict(list(zip([2, 3, 4, 5, 6, 7, 8, 9],
            "twenty thirty forty fifty sixty seventy eighty ninety".split(' '))))

# Remember to account for "hundred", "thousand" and the "and"s

def spell(n):
    """Write out n in characters. Only valid for 1-999."""
    outstring = ''
    n_hund = n // 100
    if n_hund != 0:
        outstring += ones[n_hund] + 'hundred'
    n_tens = n % 100
    if n_tens != 0 and n_hund != 0:
        outstring += 'and'
    if 1 <= n_tens <= 9:
        outstring += ones[n_tens]
    elif 10 <= n_tens <= 19:
        outstring += teens[n_tens]
    elif n_tens >= 20:
        outstring += tens[n_tens//10]
        n_ones = n_tens % 10
        if 1 <= n_ones <= 9:
            outstring += ones[n_ones]
    return outstring

total = 0
# this loop catches all spelled numbers 1-999
for i in range(1000):
    total += len(spell(i))
total += len("onethousand")
    
print("The answer is %d." % total)