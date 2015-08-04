#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


def merge_sort(lst):
    """
    Sort a list of values using merge sort.
    Return the sorted version of the list
    """
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]

    sort_left = merge_sort(left)
    sort_right = merge_sort(right)

    return merge(sort_left, sort_right)


def merge(left, right):
    """
    Helper function for merge sort. Merges two pre-sorted lists of values
    """
    sort = []
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            sort.append(left[l_index])
            l_index += 1
        else:
            sort.append(right[r_index])
            r_index += 1

    if l_index < len(left):
        sort.extend(left[l_index:])
    else:
        sort.extend(right[r_index:])

    return sort


if __name__ == '__main__':
    from timeit import Timer

    def best_case(n):
        return range(n)

    def worst_case(n):
        return range(n, 0, -1)

    print
    print "Time for best case of list of first 10 integers"
    print Timer(
        'merge_sort(best_case(10))',
        'from __main__ import merge_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 10 integers"
    print Timer(
        'merge_sort(worst_case(10))',
        'from __main__ import merge_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 100 integers"
    print Timer(
        'merge_sort(best_case(100))',
        'from __main__ import merge_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 100 integers"
    print Timer(
        'merge_sort(worst_case(100))',
        'from __main__ import merge_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 1000 integers"
    print Timer(
        'merge_sort(best_case(1000))',
        'from __main__ import merge_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 1000 integers"
    print Timer(
        'merge_sort(worst_case(1000))',
        'from __main__ import merge_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 2000 integers"
    print Timer(
        'merge_sort(best_case(2000))',
        'from __main__ import merge_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 2000 integers"
    print Timer(
        'merge_sort(worst_case(2000))',
        'from __main__ import merge_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 3000 integers"
    print Timer(
        'merge_sort(best_case(3000))',
        'from __main__ import merge_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 3000 integers"
    print Timer(
        'merge_sort(worst_case(3000))',
        'from __main__ import merge_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 4000 integers"
    print Timer(
        'merge_sort(best_case(4000))',
        'from __main__ import merge_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 4000 integers"
    print Timer(
        'merge_sort(worst_case(4000))',
        'from __main__ import merge_sort, worst_case'
    ).timeit(10) / 10

    print
    print "Time for best case of list of first 5000 integers"
    print Timer(
        'merge_sort(best_case(5000))',
        'from __main__ import merge_sort, best_case'
    ).timeit(10) / 10

    print
    print "Time for worst case of list of first 5000 integers"
    print Timer(
        'merge_sort(worst_case(5000))',
        'from __main__ import merge_sort, worst_case'
    ).timeit(10) / 10

    print "These tests approximately model O(n log(n)) behavior for all cases"
    print "so the merge sort is unbiased of how well sorted any inputs are prior"
    print "to a merge sort. The merge sort is ideal for large, poorly sorted data"
    print "sets, as compared to insertion sort which is O(n2) in worst cases."
    print "However merge sorts are more expensive with space as compared to"
    print "other algorithms, according to Wikipedia"
    print "https://en.wikipedia.org/wiki/Merge_sort"
