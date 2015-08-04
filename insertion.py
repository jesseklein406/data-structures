#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def insertion_sort(lst):
    """
    Sort a list in place using insertion sort
    """
    for i, item in enumerate(lst[1:], start=1):
        j = i
        while j > 0 and lst[j - 1] > item:
            lst[j] = lst[j - 1]
            j = j - 1
        lst[j] = item


if __name__ == '__main__':
    from timeit import Timer

    def best_case(n):
        return range(n)

    def worst_case(n):
        return range(n, 0, -1)

    print
    print "Time for best case of list of first 10 integers"
    print Timer(
        'insertion_sort(best_case(10))',
        'from __main__ import insertion_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 10 integers"
    print Timer(
        'insertion_sort(worst_case(10))',
        'from __main__ import insertion_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 100 integers"
    print Timer(
        'insertion_sort(best_case(100))',
        'from __main__ import insertion_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 100 integers"
    print Timer(
        'insertion_sort(worst_case(100))',
        'from __main__ import insertion_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 1000 integers"
    print Timer(
        'insertion_sort(best_case(1000))',
        'from __main__ import insertion_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 1000 integers"
    print Timer(
        'insertion_sort(worst_case(1000))',
        'from __main__ import insertion_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 2000 integers"
    print Timer(
        'insertion_sort(best_case(2000))',
        'from __main__ import insertion_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 2000 integers"
    print Timer(
        'insertion_sort(worst_case(2000))',
        'from __main__ import insertion_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 3000 integers"
    print Timer(
        'insertion_sort(best_case(3000))',
        'from __main__ import insertion_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 3000 integers"
    print Timer(
        'insertion_sort(worst_case(3000))',
        'from __main__ import insertion_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 4000 integers"
    print Timer(
        'insertion_sort(best_case(4000))',
        'from __main__ import insertion_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 4000 integers"
    print Timer(
        'insertion_sort(worst_case(4000))',
        'from __main__ import insertion_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 5000 integers"
    print Timer(
        'insertion_sort(best_case(5000))',
        'from __main__ import insertion_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 5000 integers"
    print Timer(
        'insertion_sort(worst_case(5000))',
        'from __main__ import insertion_sort, worst_case'
    ).timeit(10) / 10

    print "These tests approximately model O(n) behavior for best case"
    print "and O(n2) behavior for worst case, so insertion sort works well"
    print "for all sets that are reasonably sorted, or small sets that are"
    print "not very sorted, and not very well for large poorly sorted data"
