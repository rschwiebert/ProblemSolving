#!/usr/bin/python

# The problem is equivalent to counting how many times 5 appears in the factorization of n!
# The requirements also ask for log(n) performance.

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        answer = 0
        e = 1
        while 5**e <= n:
            answer += n//5**e
            e += 1
        return answer

sol = Solution()

if __name__ == "__main__":
    import timeit
    times = []
    for e in range(1,11):
        times.append(timeit.timeit('sol.trailingZeroes(10**%d)'%e, setup = 'from factorial_trailing_zeros import sol',number=100))
    for i in range(1, len(times)):
        print times[i]/times[i-1]
