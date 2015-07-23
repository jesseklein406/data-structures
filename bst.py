#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value == self.value:
            return
        elif value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                return self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                return self.right.insert(value)

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)

    def size(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return self.right.size() + 1
        if self.right is None:
            return self.left.size() + 1
        return self.left.size() + self.right.size() + 1

    def depth(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return self.right.depth() + 1
        if self.right is None:
            return self.left.depth() + 1
        return max(self.left.depth(), self.right.depth()) + 1

    def balance(self):
        if self.left is None and self.right is None:
            return 0
        if self.left is None:
            return -1 * self.right.depth()
        if self.right is None:
            return self.left.depth()
        return self.left.depth() - self.right.depth()


if __name__ == '__main__':
    from timeit import Timer
    tree_root = Node(10)
    vals = [5, 15, 3, 7, 12, 20, 2, 4, 6, 9, 11, 14, 18, 25]
    for val in vals:
        tree_root.insert(val)

    no_branches = Node(10)
    vals = range(11, 25)
    for val in vals:
        no_branches.insert(val)

    print
    print "Time for optimally filled tree with 15 nodes to search for 15th node"
    print Timer(
        'tree_root.contains(25)',
        'from __main__ import tree_root'
    ).timeit(1000)

    print
    print "Time for tree with no branches with 15 nodes to search for 15th node"
    print Timer(
        'no_branches.contains(25)',
        'from __main__ import no_branches'
    ).timeit(1000)
    print
    print "This represents time for searching with 4 recursions vs 15 recursions,"
    print "or about a ~1/4 ratio"
