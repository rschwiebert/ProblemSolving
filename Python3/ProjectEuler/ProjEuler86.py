#!/usr/bin/python
__author__ = 'ryan'

# https://projecteuler.net/problem=86

# From the integer-side boxes, consider ones for which the geodesic along the surface between opposite corners
# is an integer.


# It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions,
# up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100.
# This is the least value of M for which the number of solutions first exceeds two thousand;
# the number of solutions when M = 99 is 1975.
# Find the least value of M such that the number of solutions first exceeds one million.

# TODO improve this by bisecting to detect MAX

from library import pythag_triple_gen

total = 0


def count_possibilities(H, W, L, MAX):
    # print('inputs: {} {} {}'.format(H, W, L))
    local_total = 0
    scale = 1
    while (scale + 1) * L <= MAX:
        scale += 1
    # print('chosen scale: {}'.format(scale))
    while scale > 0:
        l = L * scale
        h = (W + H) * scale // 2
        w = (W + H) * scale - h
        while h >= 1 and w <= l <= MAX:
            # print(h, w, l)
            local_total += 1
            h -= 1
            w += 1
        scale -= 1

    return local_total


if __name__ == '__main__':
    MAX = 1818

    # # This works, trying something new
    # c = 0
    # for H, W, L in combinations_with_replacement(range(1, MAX), 3):
    #     if is_square((W + H) ** 2 + L ** 2):
    #         print(H, W, L, sqrt((W + H) ** 2 + L ** 2))
    #         c += 1
    # print(c)

    total = 0
    for a, b, c in pythag_triple_gen(limiting_function=min, max_=MAX):
        # first phase
        L = b
        H = a // 2
        W = a - H
        total += count_possibilities(H, W, L, MAX)
        # scale = 1
        # while (scale + 1) * L <= MAX:
        #     scale += 1
        #
        # while scale > 0:
        #     l = L * scale
        #     w = W * scale
        #     h = H * scale
        #     while h >= 1 and w <= l:
        #         print(h, w, l)
        #         total += 1
        #         h -= 1
        #         w += 1
        #     scale -= 1

        # second phase
        L = a
        H = b // 2
        W = b - H
        total += count_possibilities(H, W, L, MAX)

    print(total)
