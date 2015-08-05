#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def quick(lst):
    if len(lst) < 1:
        return lst

    # find median of first, last, and midpoint
    if lst[-1] < lst[0] == lst[0] < lst[len(lst) // 2]:
        pivot = 0
    if lst[0] < lst[-1] == lst[-1] < lst[len(lst) // 2]:
        pivot = len(lst) - 1
    else:
        pivot = len(lst) // 2

    left = []
    right = []
    for x in lst[:pivot] + lst[pivot + 1:]:
        if x <= lst[pivot]:
            left.append(x)
        else:
            right.append(x)

    left_sort = quick(left)
    right_sort = quick(right)

    return left_sort + [lst[pivot]] + right_sort


if __name__ == '__main__':
    from timeit import Timer
    import random

    def best_case(n):
        return range(n)

    def reverse_case(n):
        return range(n, 0, -1)

    def ones(n):
        return n * [1]

    shuffled = range(5000)
    random.shuffle(shuffled)

    def shuffled_case(n):
        return shuffled[:n]

    print
    print "Time for best case of list of first 10 integers"
    print Timer(
        'quick(best_case(10))',
        'from __main__ import quick, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 10 integers"
    print Timer(
        'quick(reverse_case(10))',
        'from __main__ import quick, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 10 integers"
    print Timer(
        'quick(ones(10))',
        'from __main__ import quick, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 10 integers"
    print Timer(
        'quick(shuffled_case(10))',
        'from __main__ import quick, shuffled_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 100 integers"
    print Timer(
        'quick(best_case(100))',
        'from __main__ import quick, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 100 integers"
    print Timer(
        'quick(reverse_case(100))',
        'from __main__ import quick, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 100 integers"
    print Timer(
        'quick(ones(100))',
        'from __main__ import quick, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 100 integers"
    print Timer(
        'quick(shuffled_case(100))',
        'from __main__ import quick, shuffled_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 1000 integers"
    print Timer(
        'quick(best_case(1000))',
        'from __main__ import quick, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 1000 integers"
    print Timer(
        'quick(reverse_case(1000))',
        'from __main__ import quick, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 997 integers"
    print Timer(
        'quick(ones(997))',
        'from __main__ import quick, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 1000 integers"
    print Timer(
        'quick(shuffled_case(1000))',
        'from __main__ import quick, shuffled_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 2000 integers"
    print Timer(
        'quick(best_case(2000))',
        'from __main__ import quick, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 2000 integers"
    print Timer(
        'quick(reverse_case(2000))',
        'from __main__ import quick, reverse_case'
    ).timeit(10) / 10

    # print
    # print "Time for all ones case of list of first 2000 integers"
    # print Timer(
    #     'quick(ones(2000))',
    #     'from __main__ import quick, ones'
    # ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 2000 integers"
    print Timer(
        'quick(shuffled_case(2000))',
        'from __main__ import quick, shuffled_case'
    ).timeit(10) / 10

    # print
    # print "Time for best case of list of first 3000 integers"
    # print Timer(
    #     'quick(best_case(3000))',
    #     'from __main__ import quick, best_case'
    # ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 3000 integers"
    print Timer(
        'quick(reverse_case(3000))',
        'from __main__ import quick, reverse_case'
    ).timeit(10) / 10

    # print
    # print "Time for all ones case of list of first 3000 integers"
    # print Timer(
    #     'quick(ones(3000))',
    #     'from __main__ import quick, ones'
    # ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 3000 integers"
    print Timer(
        'quick(shuffled_case(3000))',
        'from __main__ import quick, shuffled_case'
    ).timeit(10) / 10

    # print
    # print "Time for best case of list of first 4000 integers"
    # print Timer(
    #     'quick(best_case(4000))',
    #     'from __main__ import quick, best_case'
    # ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 4000 integers"
    print Timer(
        'quick(reverse_case(4000))',
        'from __main__ import quick, reverse_case'
    ).timeit(10) / 10

    # print
    # print "Time for all ones case of list of first 4000 integers"
    # print Timer(
    #     'quick(ones(4000))',
    #     'from __main__ import quick, ones'
    # ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 4000 integers"
    print Timer(
        'quick(shuffled_case(4000))',
        'from __main__ import quick, shuffled_case'
    ).timeit(10) / 10

    # print
    # print "Time for best case of list of first 5000 integers"
    # print Timer(
    #     'quick(best_case(5000))',
    #     'from __main__ import quick, best_case'
    # ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 5000 integers"
    print Timer(
        'quick(reverse_case(5000))',
        'from __main__ import quick, reverse_case'
    ).timeit(10) / 10

    # print
    # print "Time for all ones case of list of first 5000 integers"
    # print Timer(
    #     'quick(ones(5000))',
    #     'from __main__ import quick, ones'
    # ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 5000 integers"
    print Timer(
        'quick(shuffled_case(5000))',
        'from __main__ import quick, shuffled_case'
    ).timeit(10) / 10
