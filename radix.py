#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import math
import string


def radix_integer(lst):
    """
    Return a sorted version of a list of integers using radix sort
    """
    for i in lst:
        assert isinstance(i, int), "Not all integers"

    if len(lst) < 1:
        return lst

    exp = int(math.log10(max(lst))) + 1  # calculate largest exponent needed
    for i in range(exp):
        buckets = [[] for j in range(10)]
        for x in lst:
            buckets[x % 10 ** (i + 1) // 10 ** i].append(x)
        lst = reduce(lambda x, y: x + y, buckets)   # concatenate all buckets
    return lst


def radix_string(s):
    for c in s:
        assert isinstance(c, (str, unicode)), "Not all strings"

    if len(s) < 1:
        return s

    max_string = max([len(x) for x in s])

    # create custom ord dictionary based on standard printable characters
    # let order and priority be the default of the library module
    ordinal = dict(zip(string.printable, range(1, len(string.printable) + 1)))
    ordinal[''] = 0   # for after end of words

    for i in range(max_string - 1, -1, -1):   # use least sig digit first
        buckets = [[] for j in range(len(ordinal))]
        for item in s:
            c = item[i: i + 1]
            buckets[ordinal[c]].append(item)
        s = reduce(lambda x, y: x + y, buckets)
    return s


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
        'radix_integer(best_case(10))',
        'from __main__ import radix_integer, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 10 integers"
    print Timer(
        'radix_integer(reverse_case(10))',
        'from __main__ import radix_integer, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 10 integers"
    print Timer(
        'radix_integer(ones(10))',
        'from __main__ import radix_integer, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 10 integers"
    print Timer(
        'radix_integer(shuffled_case(10))',
        'from __main__ import radix_integer, shuffled_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 100 integers"
    print Timer(
        'radix_integer(best_case(100))',
        'from __main__ import radix_integer, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 100 integers"
    print Timer(
        'radix_integer(reverse_case(100))',
        'from __main__ import radix_integer, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 100 integers"
    print Timer(
        'radix_integer(ones(100))',
        'from __main__ import radix_integer, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 100 integers"
    print Timer(
        'radix_integer(shuffled_case(100))',
        'from __main__ import radix_integer, shuffled_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 1000 integers"
    print Timer(
        'radix_integer(best_case(1000))',
        'from __main__ import radix_integer, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 1000 integers"
    print Timer(
        'radix_integer(reverse_case(1000))',
        'from __main__ import radix_integer, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 1000 integers"
    print Timer(
        'radix_integer(ones(1000))',
        'from __main__ import radix_integer, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 1000 integers"
    print Timer(
        'radix_integer(shuffled_case(1000))',
        'from __main__ import radix_integer, shuffled_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 2000 integers"
    print Timer(
        'radix_integer(best_case(2000))',
        'from __main__ import radix_integer, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 2000 integers"
    print Timer(
        'radix_integer(reverse_case(2000))',
        'from __main__ import radix_integer, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 2000 integers"
    print Timer(
        'radix_integer(ones(2000))',
        'from __main__ import radix_integer, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 2000 integers"
    print Timer(
        'radix_integer(shuffled_case(2000))',
        'from __main__ import radix_integer, shuffled_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 3000 integers"
    print Timer(
        'radix_integer(best_case(3000))',
        'from __main__ import radix_integer, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 3000 integers"
    print Timer(
        'radix_integer(reverse_case(3000))',
        'from __main__ import radix_integer, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 3000 integers"
    print Timer(
        'radix_integer(ones(3000))',
        'from __main__ import radix_integer, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 3000 integers"
    print Timer(
        'radix_integer(shuffled_case(3000))',
        'from __main__ import radix_integer, shuffled_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 4000 integers"
    print Timer(
        'radix_integer(best_case(4000))',
        'from __main__ import radix_integer, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 4000 integers"
    print Timer(
        'radix_integer(reverse_case(4000))',
        'from __main__ import radix_integer, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 4000 integers"
    print Timer(
        'radix_integer(ones(4000))',
        'from __main__ import radix_integer, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 4000 integers"
    print Timer(
        'radix_integer(shuffled_case(4000))',
        'from __main__ import radix_integer, shuffled_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 5000 integers"
    print Timer(
        'radix_integer(best_case(5000))',
        'from __main__ import radix_integer, best_case'
    ).timeit(10) / 10

    print
    print "Time for reverse case of list of first 5000 integers"
    print Timer(
        'radix_integer(reverse_case(5000))',
        'from __main__ import radix_integer, reverse_case'
    ).timeit(10) / 10

    print
    print "Time for all ones case of list of first 5000 integers"
    print Timer(
        'radix_integer(ones(5000))',
        'from __main__ import radix_integer, ones'
    ).timeit(10) / 10

    print
    print "Time for shuffled case of list of first 5000 integers"
    print Timer(
        'radix_integer(shuffled_case(5000))',
        'from __main__ import radix_integer, shuffled_case'
    ).timeit(10) / 10

    print "These test cases show similar behavior for sorted, reverse sorted,"
    print "and shuffled data sets. However, the case for all equal values"
    print "performs exceptionally well. Possibly because so many of the"
    print "buckets collapse out early, reducing the number of iterations."
    print "All cases show several times faster behavior than the alternatives,"
    print "with a large advantage for similar data within a list. The time"
    print "complexity approaches O(n) for cases tested."
