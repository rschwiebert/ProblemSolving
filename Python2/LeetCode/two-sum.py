__author__ = 'ryan'


class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        n = len(num)
        myhash = dict((target-a, j) for (j, a) in enumerate(num))
        for i in range(n):
            try:
                a, b = (i+1, myhash[num[i]] + 1,)
                if a != b:
                    return tuple(sorted([a, b]))
            except KeyError:
                continue
