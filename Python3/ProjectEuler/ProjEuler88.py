#!/usr/bin/python
__author__ = 'ryan'

# https://projecteuler.net/problem=88
# What is the sum of all the minimal product-sum numbers for 2<=k<=12000?

# Observation: for $n$ length tuples, (1,1,1,...,2,n) is always a solution. Therefore we are limited to sum-numbers
# less or equal to 24000. For each n between 2 and 12000, we can generate all nondecreasing lists with product n,
# and then append 1's until its sum matches its product (which we know is n).  This generates all the relevant
# sum-product numbers for the problem.

from copy import deepcopy
from bisect import insort

if __name__ == '__main__':
    factorizations = [[[i, ]] for i in range(24001)]
    results = [50000] * 12001

    for i in range(2, 24001):

        # While we're here, check what sum-product numbers we have developeds so far
        for fzn in factorizations[i]:
            tot = sum(fzn)
            length = len(fzn)
            diff = i - tot
            length += diff
            if length > 12000:
                continue
            if i < results[length]:
                results[length] = i

        # Advance multiple by multiple filling out factorizations further down the list
        j = 2
        ind = i * j
        while ind <= 24000:
            copies = deepcopy(factorizations[i])
            for cpy in copies:
                insort(cpy, j)  # Keeping lists sorted aids de-duplication in the next loop
                if cpy not in factorizations[ind]:
                    factorizations[ind].append(cpy)

            j += 1
            ind = i * j

    # Along the way, I discovered the entries of `results` are no necessarily nondecreasing!
    deduped_results = set(results[2:])
    answer = sum(deduped_results)
    print('Answer: {}'.format(answer))
