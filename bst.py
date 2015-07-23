#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals


class Node(object):
    """
    A Node class that will create instances of nodes, all of which can
    represent the root of a binary search tree.
    """
    def __init__(self, value):
        """
        Make a new nodes object with a value given as the argument
        """
        self.value = value
        self.left = None    # initially set pointers to None
        self.right = None

    def insert(self, value):
        """
        Insert a new node into a tree with value given as argument if value
        is not present, else do nothing
        """
        if value == self.value:
            return   # if value exists, do nothing
        elif value < self.value:
            if self.left is None:
                self.left = Node(value)  # create value at empty pointer
            else:
                return self.left.insert(value)  # repeat for next node
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                return self.right.insert(value)

    def contains(self, value):
        """
        Check a tree for a node with value given as argument, return True
        if the value is present, False if not
        """
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
        """
        Return the number of nodes in a tree
        """
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return self.right.size() + 1   # Add 1 to the sum of branch sizes
        if self.right is None:             # to account for self
            return self.left.size() + 1
        return self.left.size() + self.right.size() + 1

    def depth(self):
        """
        Return the depth of the tree
        """
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return self.right.depth() + 1   # A single node has a depth of 1
        if self.right is None:
            return self.left.depth() + 1
        return max(self.left.depth(), self.right.depth()) + 1

    def balance(self):
        """
        Return a positive balance if the root's left side is deeper,
        negative balance if the right side is deeper, and zero if
        the tree is balanced
        """
        if self.left is None and self.right is None:
            return 0
        if self.left is None:
            return -1 * self.right.depth()
        if self.right is None:
            return self.left.depth()
        return self.left.depth() - self.right.depth()

    def pre_order(self):
        parent_stack = []
        while parent_stack or self is not None:
            if self is not None:
                yield self
                if self.right is not None: 
                    parent_stack.append(self.right)
                self = self.left
            else:
                self = parent_stack.pop()

    def in_order(self):
        parent_stack = []
        while parent_stack or self is not None:
            if self is not None:
                parent_stack.append(self)
                self = self.left
            else:
                self = parent_stack.pop()
                yield self
                self = self.right

    def post_order(self):
        parent_stack = []
        last_node = None
        while parent_stack or self is not None:
            if self is not None:
                parent_stack.append(self)
                self = self.left
            else:
                peek = parent_stack[-1]
                if peek.right is not None and last_node is not peek.right:
                    self = peek.right
                else:
                    yield peek
                    last_node = parent_stack.pop()

    def breadth_order(self):
        queue = []


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
